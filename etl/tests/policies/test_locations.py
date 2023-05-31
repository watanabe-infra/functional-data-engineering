from etl.policies.locations import JpRegionPolicy


def test_jp_region_north_success(iso3166_2_constants):

    assert JpRegionPolicy.is_northern_japan(iso3166_2_constants.hokkaido)


def test_jp_region_north_fail(iso3166_2_constants):

    assert JpRegionPolicy.is_northern_japan(iso3166_2_constants.okinawa)
