# tools/fetchers.py
import datetime
import random

def fetch_latest_news(company: str, limit=5):
    now = datetime.datetime.utcnow()
    samples = [
        f"{company} launches new AI product",
        f"{company} reports strong Q4 earnings",
        f"{company} expands into Europe",
        f"{company} faces supply chain challenges",
        f"{company} announces strategic partnership"
    ]

    news = []
    for i in range(limit):
        news.append({
            "title": samples[i],
            "summary": "This is a sample summary used for demonstration.",
            "published_at": (now - datetime.timedelta(hours=i*6)).isoformat(),
            "url": "https://example.com/news"
        })
    return news


def fetch_stock_data(company: str, days=7):
    base = 100 + random.uniform(-10, 10)
    prices = []
    for d in range(days):
        prices.append({
            "date": (datetime.date.today() - datetime.timedelta(days=d)).isoformat(),
            "close": round(base + random.uniform(-4, 4), 2)
        })

    change = round(((prices[-1]["close"] - prices[0]["close"]) / prices[0]["close"]) * 100, 2)

    return {
        "symbol": company[:6].upper(),
        "prices": prices,
        "latest_close": prices[-1]["close"],
        "7d_change_pct": change
    }
