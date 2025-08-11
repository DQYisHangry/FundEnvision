import mysql.connector
from model.etf_nav import EtfNav

# This file defines a simple class for connecting to a MySQL database
# and retrieving ETF NAV data by ticker symbol.
# It reads data from the 'etf_nav' table and returns a list of EtfNav objects.

class MysqlRepository:

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'wcwcwc',
            'host': 'localhost',
            'port': 3306,
            'database': 'funds_db'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    # When the class is deleted or done being used, close the connection
    def __del__(self):
        self.cursor.close()
        self.connection.close()

    # This function gets all NAV entries for one ticker symbol
    def list_nav_by_ticker(self, ticker):
        sql = "SELECT ticker, fund_name, nav_date, nav FROM etf_nav WHERE ticker = %s ORDER BY nav_date DESC"
        self.cursor.execute(sql, (ticker,))
        result = []

        for row in self.cursor:
            entry = EtfNav(row[0], row[1], row[2], row[3])
            result.append(entry)

        return result