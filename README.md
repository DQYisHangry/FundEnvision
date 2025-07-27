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
| NAV (Net Asset Value)                          | 10.56 (USD)              |
| Historical NAVs                                | Past 30 days             |
| Subscription/Redemption summaries (aggregated) | "+500M inflow this week" |

### Use cases
Use Case 1: View Fund Summary

As a general user, I want to search for a fund by name or code and view:
Its latest NAV/Fund type/category Aggregate subscription/redemption summaries

Use Case 2: View Historical NAV
As an analyst, I want to view a graph or table of NAV values over time for a fund to observe trends.

Use Case 3: Update Fund Data
As a data engineer, I want to trigger the scraper to re-collect data and store the updated NAV and summaries in the database.


