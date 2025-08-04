# FundEnvision


## What This Project Does

- Collects historical NAV data for a few selected ETFs using [yfinance](https://pypi.org/project/yfinance/).
- Cleans and stores the data into a MySQL database (`funds_db`) with a single table `etf_nav`.
- Provides a simple repository interface to query NAV data by ticker.
- Includes basic Pytest tests to verify that the database integration works.

## What Data Is Collected?

| Field        | Example          |
| ------------ | ---------------- |
| Ticker       | SPY              |
| Fund Name    | SPDR S&P 500 ETF |
| Date         | 2024-08-01       |
| NAV          | 512.23           |

Only data for a few ETFs (e.g., SPY, QQQ, VTI) is included for demonstration. Each ETF includes approximately one year of daily NAVs.

## Use Cases

### Use Case 1: View Historical NAV

As a user, I want to retrieve the NAV history of a given ETF ticker (e.g., `SPY`) so I can analyze its trends.

### Use Case 2: Verify Data Is Stored Correctly

As a developer, I want to run a test to confirm that data has been inserted into the database and can be retrieved via repository methods.

