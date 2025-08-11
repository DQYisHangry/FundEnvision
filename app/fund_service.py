from decimal import Decimal
from model.etf_nav import EtfNav

class FundService:

    def __init__(self, repo):
        self.repo = repo

    #Use case 1: Get the latest NAV for a given ticker
    def get_latest_nav(self, ticker):
        navs = list(self.repo.fetch_navs(ticker))

        #If nothing is returned, there is no latest NAV
        if navs == []:
            return None

        #Start with the first item as the "latest"
        latest = navs[0]

        #Loop through the rest and pick the one with the newest date
        i = 1
        while i < len(navs):
            item = navs[i]
            if item.nav_date > latest.nav_date:
                latest = item
            i = i + 1

        #Give back the record with the greatest (most recent) date
        return latest

    #Use case 2: Get historical NAVs within a date range (sorted by date)
    def get_historical_nav(self, ticker, start, end):
        #Ask the repo for items in the date range (inclusive/exclusive decided by repo)
        navs = list(self.repo.fetch_navs(ticker, start, end))

        #Sort by date from earliest to latest using a simple bubble sort (beginner style)
        n = len(navs)
        a = 0
        while a < n:
            b = 0
            while b < n - 1:
                left = navs[b]
                right = navs[b + 1]
                #If the left date is after the right date, swap them
                if left.nav_date > right.nav_date:
                    temp = navs[b]
                    navs[b] = navs[b + 1]
                    navs[b + 1] = temp
                b = b + 1
            a = a + 1

        #Return the sorted list so index 0 is earliest and last index is latest
        return navs

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
        last = series[len(series) - 1].nav

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