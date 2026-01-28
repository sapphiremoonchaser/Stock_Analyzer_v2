from stock_analyzer_v2.core.fetcher import fetch_basic_stock_info

if __name__ == "__main__":
    tickers = [
        "AAPL",
        "MSFT",
        "GOOGL",
        "TSLA"
    ]

    for t in tickers:
        data = fetch_basic_stock_info(t)
        if data:
            print(f"\n{t}")
            print("-" * 40)
            for k, v in data.items():
                print(f"{k:18} : {v}")

        else:
            print(f"Failed to fetch {t}")
