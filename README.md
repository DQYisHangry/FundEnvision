# FundEnvision


### This project is a Python-based application that:
- Scrapes publicly available fund data from financial websites.
- Stores the scraped data in a SQLite database.
- Allows processing and querying of the stored data (e.g., search by fund code, view historical NAV).
- Provides a simple web interface (via Flask) to search and display fund details.

### What Data Is Collected?

| Scraped Data                                   | Example                  |
| ---------------------------------------------- | ------------------------ |
| Fund name                                      | "ABC Growth Fund"        |
| Fund code                                      | "ABC123"                 |
| Fund type/category                             | "Equity", "Bond", etc.   |
| NAV (Net Asset Value)                          | 10.56            |
| Historical NAVs                                | Past 30 days             |


### Use cases
Use Case 1: View latest NAV for a ticker
As a user, I want to quickly get the most recent NAV data point for an ETF.


Use Case 2: View Historical NAV
As an analyst, I want to view a graph or table of NAV values over time for a fund to observe trends.

Use Case 3: Simple stats over a date range
As a user, I want to get a tiny summary for a period (count of days, first/last NAV, absolute and % change).
