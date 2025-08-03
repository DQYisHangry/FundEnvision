import yfinance as yf
import pandas as pd

# 这里列出你想抓取的 ETF 代码
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
df.to_csv("yahoo_etf_navs.csv", index=False, float_format="%.2f")
print("Saved to yahoo_etf_navs.csv")
