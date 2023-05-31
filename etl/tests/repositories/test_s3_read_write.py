from apache_beam.portability.api.org.apache import beam
from apache_beam.testing.util import equal_to, assert_that

from etl.repositories.s3_read_write import S3ReadWrite

from apache_beam.pvalue import PCollection
from apache_beam.testing.test_pipeline import TestPipeline


def test_s3_write():
    with TestPipeline as p:
        WORDS: list[str] = ["Hello", "World"]
        pCol: PCollection = beam.Create(WORDS)

        client: S3ReadWrite = S3ReadWrite()
        result = pCol | beam.Map()

        assert_that(
            result,
            equal_to(
                WORDS
            )
        )