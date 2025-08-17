from flask import Flask, jsonify, request
from decimal import Decimal
from datetime import date

from app.fund_service import FundService
from db.mysql_repository import MysqlRepository

service = FundService(MysqlRepository())
from datetime import date

def parse_date(s: str | None) -> date | None:
    if not s:
        return None
    return date.fromisoformat(s)

def to_float(v):
    from decimal import Decimal
    return float(v) if isinstance(v, Decimal) else v

app = Flask(__name__)

@app.get("/api/v1/nav/<ticker>")
def latest_nav(ticker: str):
    nav = service.get_latest_nav(ticker.upper())
    if not nav:
        return jsonify({"error": "not found"}), 404
    def to_float(v): return float(v) if isinstance(v, Decimal) else v
    return jsonify({
        "ticker": nav.ticker,
        "nav_date": nav.nav_date.isoformat(),
        "nav": to_float(nav.nav),
        "fund_name": getattr(nav, "fund_name", None),
        "source": getattr(nav, "source", None),
    }), 200


@app.get("/api/v1/nav/<ticker>/summary")
def summary_nav(ticker: str):
    start = parse_date(request.args.get("start"))
    end   = parse_date(request.args.get("end"))
    if not (start and end) or start > end:
        return jsonify({"error": "invalid date range"}), 400
    out = service.get_nav_summary(ticker.upper(), start, end)
    out = {k: to_float(v) for k, v in out.items()}
    return jsonify(out), 200

if __name__ == "__main__":
    app.run(debug=True)
