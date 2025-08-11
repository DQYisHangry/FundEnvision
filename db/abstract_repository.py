from datetime import date
from typing import Optional, List
from model.etf_nav import EtfNav


class Repository:
    def fetch_navs(
        self,
        ticker: str,
        start: Optional[date] = None,
        end: Optional[date] = None,
    ) -> List[EtfNav]:
        """
        Return NAV rows for `ticker`.
        """
        raise NotImplementedError("Subclasses must implement fetch_navs().")


    def list_nav_by_ticker(self, ticker: str) -> List[EtfNav]:
        """
        Use fetch_navs(). Kept for backward compatibility with older tests.
        """
        return self.fetch_navs(ticker)
