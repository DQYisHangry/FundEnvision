from db.mysql_repository import MysqlRepository

#This test checks whether the MysqlRepository class can successfully
#connect to the MySQL database and retrieve NAV records for a given ETF ticker.
#It verifies that:
#   1. The result is a list
#   2. The list is not empty for a known valid ticker

def test_list_nav_by_ticker():
    repo = MysqlRepository()
    results = repo.list_nav_by_ticker("SPY")
    assert isinstance(results, list)
    assert len(results) > 0
