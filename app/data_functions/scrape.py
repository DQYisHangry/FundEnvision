import yfinance as yf
import pandas as pd

# Fetched the past 1 year of historical closing prices (NAV) for a list of ETFs using the yfinance API.
# For each ETF, it:
#   - Gets the fund name and closing price history
#   - Renames and rounds the "Close" price as "NAV"
#   - Adds the ticker and fund name to the data
# Then it combines all ETF data into one DataFrame and saves it
# to 'db/etf_nav_clean.csv' for later use.

tickers = ["SPY", "QQQ", "VTI"]

all_df = []
for sym in tickers:
    t = yf.Ticker(sym)
    name = t.info.get("longName", sym)
    hist = t.history(period="1y")[["Close"]].reset_index()
    hist["Close"] = hist["Close"].round(2)
    hist["Ticker"] = sym
    hist["Fund Name"] = name
    all_df.append(hist.rename(columns={"Close": "NAV"}))

df = pd.concat(all_df, ignore_index=True)
df = df[["Ticker", "Fund Name", "Date", "NAV"]]
df.to_csv("db/etf_nav_clean.csv", index=False)

