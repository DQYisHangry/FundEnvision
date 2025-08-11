from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional

@dataclass(frozen=True)
class EtfNav:
    ticker: str
    nav_date: date
    nav: Decimal
    fund_name: Optional[str] = None
    source: Optional[str] = None
