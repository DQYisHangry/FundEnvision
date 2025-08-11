from datetime import date
from decimal import Decimal
from model.etf_nav import EtfNav
from app.fund_service import FundService

class FakeRepo:
    def __init__(self, items):
        self.items = items

    def fetch_navs(self, ticker, start=None, end=None):
        res = [x for x in self.items if x.ticker == ticker]
        if start:
            res = [x for x in res if x.nav_date >= start]
        if end:
            res = [x for x in res if x.nav_date <= end]
        return res

def make_series():
    return [
        EtfNav("QQQ", date(2025, 8, 5),  Decimal("502.10")),
        EtfNav("QQQ", date(2025, 8, 6),  Decimal("503.00")),
        EtfNav("QQQ", date(2025, 8, 7),  Decimal("501.50")),
    ]

def test_get_latest_nav():
    svc = FundService(FakeRepo(make_series()))
    latest = svc.get_latest_nav("QQQ")
    assert latest.nav_date == date(2025, 8, 7)
    assert latest.nav == Decimal("501.50")

def test_get_historical_nav_sorted_and_filtered():
    svc = FundService(FakeRepo(make_series()))
    out = svc.get_historical_nav("QQQ", date(2025, 8, 6), date(2025, 8, 7))
    assert [x.nav_date for x in out] == [date(2025, 8, 6), date(2025, 8, 7)]

def test_get_nav_summary():
    svc = FundService(FakeRepo(make_series()))
    summary = svc.get_nav_summary("QQQ", date(2025, 8, 5), date(2025, 8, 7))
    assert summary["count"] == 3
    assert summary["first"] == Decimal("502.10")
    assert summary["last"] == Decimal("501.50")
    assert summary["abs_change"] == Decimal("501.50") - Decimal("502.10")
    assert summary["pct_change"] < Decimal("0")
