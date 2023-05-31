import argparse

from apache_beam import coders, PCollection
from apache_beam.io.jdbc import ReadFromJdbc
from apache_beam.options.pipeline_options import SetupOptions, PipelineOptions
import apache_beam as beam

from etl.entities.request_master import GasConstructionRequest
from etl.policies.locations import JpRegionPolicy
from etl.repositories.s3_read_write import S3ReadWrite


def main(argv: list = None, save_main_session=True):
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    known_args, pipeline_args = parser.parse_known_args(argv)

    # Mainly for when using dataflow
    # https://cloud.google.com/dataflow/docs/guides/common-errors
    pipeline_options: PipelineOptions = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session

    coders.registry.register_code(GasConstructionRequest, coders.RowCoder)

    with beam.Pipeline(options=pipeline_options) as p:
        # Read from source
        # https://beam.apache.org/releases/pydoc/2.47.0/apache_beam.io.jdbc.html#apache_beam.io.jdbc.ReadFromJdbc
        rows: tuple = p | ReadFromJdbc(
            table_name='events',
            driver_class_name='org.postgresql.Driver',
            jdbc_url='jdbc:postgresql://localhost:5432/example',
            username='SOME_USER',
            password='SOME_PASSWORD',
        )

        # Do business logic
        events: PCollection = rows | beam.Filter(
            lambda x: JpRegionPolicy.is_northern_japan(x.construction_prefecture))

        # Put to S3
        client: S3ReadWrite = S3ReadWrite()
        events | beam.Map(client.write)


if __name__ == '__main__':
    main()
