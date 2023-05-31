
# Constants
ISO3166_2_HOKKAIDO_NAME: str = 'Hokkaido'


class JpRegionPolicy:
    @staticmethod
    def is_northern_japan(iso3166_2_pref_name: str) -> bool:
        """
        is_northern_japan checks if the input parameter is northern region of Japan

        :param iso3166_2_pref_name: str
        :return: bool
        """
        return iso3166_2_pref_name in [ISO3166_2_HOKKAIDO_NAME]
