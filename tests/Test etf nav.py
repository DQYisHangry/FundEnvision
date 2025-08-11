"""This test is to see if the etf data in mysql are in good order"""

from datetime import date
from decimal import Decimal
from model.etf_nav import EtfNav

def test_etf_nav_basic_fields():
    nav = EtfNav("SPY", date(2024, 12, 31), Decimal("575.12"))
    assert nav.ticker == "SPY"
    assert nav.nav_date.year == 2024
    assert nav.nav == Decimal("575.12")
