class EtfNav:
    def __init__(self, ticker, fund_name, nav_date, nav):
        self.ticker = ticker
        self.fund_name = fund_name
        self.nav_date = nav_date
        self.nav = nav

    def __repr__(self):
        return f"EtfNav(ticker={self.ticker}, fund_name={self.fund_name}, nav_date={self.nav_date}, nav={self.nav})"
