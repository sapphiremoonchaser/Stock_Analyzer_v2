from unittest.mock import MagicMock
import pandas as pd

from stock_analyzer_v2.core.yfinance_fetcher import YFinanceFetcher
from stock_analyzer_v2.data.enums.metrics import StockMetric


def test_fetch_info_metric(monkeypatch):
    mock_ticker = MagicMock()
    mock_ticker.info = {
        "trailingPE": 25.0
    }

    monkeypatch.setattr(
        "stock_analyzer_v2.core.yfinance_fetcher.yf.Ticker",
        lambda _: mock_ticker
    )

    fetcher = YFinanceFetcher("AAPL")
    value = fetcher.fetch_metric(StockMetric.pe_ratio)

    assert value == 25.0


def test_fetch_financial_time_series(monkeypatch):
    df = pd.DataFrame(
        {
            pd.Timestamp("2023-12-31"): [100],
            pd.Timestamp("2022-12-31"): [90]
        },
        index=['Total Revenue']
    )

    mock_ticker = MagicMock()
    mock_ticker.financials = df

    monkeypatch.setattr(
        "stock_analyzer_v2.core.yfinance_fetcher.yf.Ticker",
        lambda _: mock_ticker
    )

    fetcher = YFinanceFetcher("AAPL")
    revenue = fetcher.fetch_metric(StockMetric.revenue)

    assert revenue.iloc[0] == 90 or revenue.iloc[0] == 100