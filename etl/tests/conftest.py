import dataclasses

import pytest


# FIXME duplicate
@dataclasses.dataclass
class Iso31662SubdivisionName:
    """
    https://en.wikipedia.org/wiki/ISO_3166-2:JP
    """
    hokkaido: str = 'HOKKAIDO'
    okinawa: str = 'OKINAWA'


@pytest.fixture()
def iso31662_constants():
    return Iso31662SubdivisionName()
