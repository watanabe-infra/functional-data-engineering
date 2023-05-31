from apache_beam.io.aws.s3io import S3IO


class S3ReadWrite:
    def __init__(self):
        self._uploader = S3IO()

    def write(self, contents: str, s3_key: str = None) -> None:
        """

        :param contents:
        :param s3_key:
        :return:
        """
        # Use input key if specified otherwise do some business logic
        s3_key: str = "MY_KEY" if s3_key is None else s3_key

        with self._uploader.open(s3_key, 'w') as fd:
            fd.write(contents)
