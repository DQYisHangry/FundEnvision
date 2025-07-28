# fund_data.py

"""Purpose:
    Defines core data object classes for the Fund Data Envision project.
"""

from enum import Enum
from datetime import datetime


class Fund:
    """
    Represents a mutual fund. Each fund is uniquely identified by its fund_code and name.
    """
    def __init__(self, fund_code: str, name: str):
        self.fund_code = fund_code
        self.name = name


class NAVRecord:
    """
    Represents a Net Asset Value (NAV) record for a specific fund on a specific date.
    """
    def __init__(self, fund_code: str, date: datetime, nav: float):
        self.fund_code = fund_code
        self.date = date
        self.nav = nav


class SubscriptionSummary:
    """
    Represents a high-level summary of subscription/redemption flows for a fund.
    """
    def __init__(self, fund_code: str, date: datetime, net_flow: str):
        self.fund_code = fund_code
        self.date = date
        self.net_flow = net_flow