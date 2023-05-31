from datetime import datetime
from typing import NamedTuple


class GasConstructionRequest(NamedTuple):
    construction_date: datetime
    customer_address: str
    construction_company: str
    construction_prefecture: str
