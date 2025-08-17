from decimal import Decimal
from model.etf_nav import EtfNav
from datetime import date
from typing import List


class FundService:

    def __init__(self, repo):
        self.repo = repo

    #Use case 1: Get the latest NAV for a given ticker
    def get_latest_nav(self, ticker: str):
        navs = list(self.repo.fetch_navs(ticker))
        if not navs:
            return None
        return max(navs, key=lambda x: x.nav_date)

    #Use case 2: Get historical NAVs within a date range (sorted by date)
    def get_historical_nav(self, ticker: str, start: date, end: date) -> List[EtfNav]:
        return sorted(self.repo.fetch_navs(ticker, start, end), key=lambda x: x.nav_date)


    #Use case 3: Simple stats over a date range
    def get_nav_summary(self, ticker, start, end):
        #First get the sorted historical series using the method above
        series = self.get_historical_nav(ticker, start, end)

        #Prepare a default result in case there is no data
        result = {
            "count": 0,
            "first": None,
            "last": None,
            "abs_change": None,
            "pct_change": None
        }

        #If the series is empty, just return the default result
        if series == []:
            return result

        #Take the first and last NAV values from the sorted list
        first = series[0].nav
        last = series[-1].nav

        #Compute absolute change (last minus first)
        abs_change = last - first

        #Compute percentage change; avoid division by zero
        if first == 0:
            pct_change = None
        else:
            pct_change = abs_change / first

        #Fill in the dictionary with simple stats
        result["count"] = len(series)
        result["first"] = first
        result["last"] = last
        result["abs_change"] = abs_change
        result["pct_change"] = pct_change

        return result