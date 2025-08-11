from typing import Optional, List
from datetime import date, datetime
from decimal import Decimal
import mysql.connector

from db.abstract_repository import Repository
from model.etf_nav import EtfNav


class MysqlRepository(Repository):
    def __init__(self):
        config = {
            "user": "root",
            "password": "Wcnmnmsl1!",
            "host": "localhost",
            "port": 3306,
            "database": "funds_db",
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        try:
            self.cursor.close()
        except Exception:
            pass
        try:
            self.connection.close()
        except Exception:
            pass

    def fetch_navs(
        self,
        ticker: str,
        start: Optional[date] = None,
        end: Optional[date] = None,
    ) -> List[EtfNav]:
        sql = """
            SELECT ticker, fund_name, nav_date, nav
            FROM etf_nav
            WHERE ticker = %s
        """
        params = [ticker]
        if start is not None:
            sql += " AND nav_date >= %s"
            params.append(start)
        if end is not None:
            sql += " AND nav_date <= %s"
            params.append(end)
        sql += " ORDER BY nav_date ASC"


        self.cursor.execute(sql, tuple(params))

        result: List[EtfNav] = []
        for (t, f, d, n) in self.cursor:
            nav_val = n if isinstance(n, Decimal) else Decimal(str(n))
            if isinstance(d, datetime):
                d = d.date()
            result.append(EtfNav(
                ticker=t,
                nav_date=d,
                nav=nav_val,
                fund_name=f,
            ))
        return result

    def list_nav_by_ticker(self, ticker: str) -> List[EtfNav]:
        return self.fetch_navs(ticker)
