
"""PLEASE IGNORE THIS TEST FOR NOW. THIS TEST IS CURRENTLY UNDER CONSTRUCTION DUE TO CHANGES OF THE PROJECT.
THIS IS THE 1st VERSION OF THE TEST"""



"""Purpose of this test:
    The goal here is to make sure our data object classes (Fund, NAVRecord, SubscriptionSummary)
    are well-formed and correctly initialized.

    At this stage, I haven't implent the web scraper yet so I'm not writing test for:
        - Whether data is accessible via web interface
        - Whether data is shown on a page
        - Whether data is stored in a database
        - Whether data is processed, calculated, or filtered
"""

from app.fund_data import Fund, NAVRecord, SubscriptionSummary
from datetime import datetime

def test_fund_object_structure():
    f = Fund(fund_code="FND001", name="Global Equity Fund")
    assert hasattr(f, "fund_code")
    assert hasattr(f, "name")
    assert isinstance(f.fund_code, str)
    assert isinstance(f.name, str)

def test_nav_record():
    nav = NAVRecord(fund_code="FND001", date=datetime(2025, 5, 5), nav=13.24)
    assert isinstance(nav.date, datetime), "Date must be a datetime object"
    assert isinstance(nav.nav, float), "NAV must be a float"

    def has_two_or_fewer_decimal_places(val: float) -> bool: ##Making sure NAV have at most 2 decimal places
        return len(str(val).split(".")[-1]) <= 2

    assert has_two_or_fewer_decimal_places(nav.nav), "NAV must have at most 2 decimal places"


def test_subscription_summary():
    summary = SubscriptionSummary(fund_code="FND001", date=datetime(2025, 7, 1), net_flow="+300M")
    assert isinstance(summary.fund_code, str)
    assert isinstance(summary.date, datetime), "Date must be a datetime object"
    assert isinstance(summary.net_flow, str), "Net flow must be a string"