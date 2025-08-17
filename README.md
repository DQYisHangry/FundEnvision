# FundEnvision


## This project is a Python-based application that:
Scrapes publicly available fund data from financial websites.

Stores the scraped data in a relational database (MySQL by default; SQLite can be used for demos).

Allows processing and querying of the stored data (e.g., search by fund code, view historical NAV).

Provides a simple web interface / API (via Flask) to query and display fund details.

## What Data Is Collected?

| Scraped Data                                   | Example                  |
| ---------------------------------------------- | ------------------------ |
| Fund name                                      | "ABC Growth Fund"        |
| Fund code                                      | "ABC123"                 |
| Fund type/category                             | "Equity", "Bond", etc.   |
| NAV (Net Asset Value)                          | 10.56            |
| Historical NAVs                                | Past 30 days             |


## Use cases
Use Case 1: View latest NAV for a ticker
As a user, I want to quickly get the most recent NAV data point for an ETF.


Use Case 2: View Historical NAV
As an analyst, I want to view a graph or table of NAV values over time for a fund to observe trends.


Use Case 3: Simple stats over a date range
As a user, I want to get a tiny summary for a period (count of days, first/last NAV, absolute and % change).


## Requirements
```python >= 3.10
pip install -r requirements.txt
pip install Flask mysql-connector-python
```

## Run the Flask API

This Flask API exposes two endpoints implemented in web/api_min.py:

Latest NAV (Use Case 1)

Range Summary (Use Case 3)

```#ensure web/ is a package (has __init__.py)
python -m web.api_min
#Server base URL:http://127.0.0.1:5000
```

## API Documentation
### Conventions

Versioning: /api/v1/...

Dates: ISO YYYY-MM-DD

Numbers: Decimal values are returned as JSON numbers

Errors: JSON object with "error" and an appropriate HTTP status


### 1) Get latest NAV for a specific ticker — Use Case 1

`GET /api/v1/nav/{ticker}
`

### Path params

`ticker (string, required), e.g. QQQ
`

### Responses

200 - OK

```
{"ticker": "QQQ",
  "nav_date": "2025-08-01",
  "nav": 553.88,
  "fund_name": "Invesco QQQ Trust",
  "source": null}

```

400 - Bad Request：

`{"error": "not found"}
`

curl：

`curl -i http://127.0.0.1:5000/api/v1/nav/QQQ
`
`curl -i http://127.0.0.1:5000/api/v1/nav/NOPE
`


### 2）Get NAV summary over a date range for a ticker — Use Case 3
`GET /api/v1/nav/{ticker}/summary?start=YYYY-MM-DD&end=YYYY-MM-DD
`

### Query params
```start (date, required)

end (date, required; must be ≥ start)
```

### Responses
200 OK

```
{"count": 6,
  "first": 550.10,
  "last": 553.88,
  "abs_change": 3.78,
  "pct_change": 0.00686
}
```


400 - Bad Request：

`{ "error": "invalid date range" }
`

curl：

`curl -i "http://127.0.0.1:5000/api/v1/nav/QQQ/summary?start=2025-07-29&end=2025-08-07"
`
