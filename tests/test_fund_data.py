# test_fund_data.py
"""Purpose of this test:
    The goal here is to make sure our data object classes (Fund, NAVRecord, SubscriptionSummary)
    are well-formed and correctly initialized.

    At this stage, I haven't implent the web scraper yet so I'm not writing test for:
        - Whether data is accessible via web interface
        - Whether data is shown on a page
        - Whether data is stored in a database
        - Whether data is processed, calculated, or filtered

    However, I have designed these classes to support those goals later.
    Once these classes pass these sanity checks, we will move on to integration with:
        - SQLite3 for storage
        - Flask for web access
        - Scraper module for data ingestion
"""

from app.fund_data import Fund, NAVRecord, SubscriptionSummary
from datetime import datetime #This is for transaction time


class Fund:
    """Represents a mutual fund. Each fund is uniquely identified by its fund_code and name."""
    def __init__(self, fund_code: str, name: str):
        self.fund_code = fund_code
        self.name = name


class NAVRecord:
    """Represents a Net Asset Value (NAV) record for a specific fund on a specific date."""
    def __init__(self, fund_code: str, date: datetime, nav: float):
        self.fund_code = fund_code
        self.date = date
        self.nav = nav


class SubscriptionSummary:
    """Represents a high-level summary of subscription/redemption flows for a fund. net_flow is a string like '+300M' or '-150M'."""
    def __init__(self, fund_code: str, date: datetime, net_flow: str):
        self.fund_code = fund_code
        self.date = date
        self.net_flow = net_flow