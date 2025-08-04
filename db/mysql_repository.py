#The class connects to a MySQL database and allows us to retrieve ETF NAV data
#by fund ticker. It implements the Repository interface,
#and is responsible for executing SQL queries and returning the results as EtfNav objects.

from db.abstract_repository import Repository
from db.etf_nav import EtfNav
import mysql.connector

class MysqlRepository(Repository):
#Set up the database connection configuration
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'Wcnmnmsl1!',
            'host': 'localhost',
            'port': 3306,
            'database': 'funds_db'
        }
        #Connect to the database and store the connection and cursor
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def list_nav_by_ticker(self, ticker: str) -> list[EtfNav]:#Convert each row from the result into an EtfNav objec
        sql = "SELECT ticker, fund_name, nav_date, nav FROM etf_nav WHERE ticker = %s ORDER BY nav_date DESC"
        self.cursor.execute(sql, (ticker,))
        result = []
        for (ticker, fund_name, nav_date, nav) in self.cursor:
            entry = EtfNav(ticker, fund_name, nav_date, nav)
            result.append(entry)
        return result
