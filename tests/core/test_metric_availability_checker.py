from unittest.mock import MagicMock

from stock_analyzer_v2.core.metric_availability_checker import (
    MetricAvailabilityChecker
)
from stock_analyzer_v2.data.enums.metrics import StockMetric


def test_metric_availability_checker():
    mock_fetcher = MagicMock()
    mock_fetcher.fetch_metric.side_effect = lambda metric: (
        10 if metric == StockMetric.pe_ratio else None
    )

    checker = MetricAvailabilityChecker(mock_fetcher)

    result = checker.check(
        [
            StockMetric.pe_ratio,
            StockMetric.free_cash_flow,
        ]
    )

    assert result.available == {StockMetric.pe_ratio}
    assert result.missing == {StockMetric.free_cash_flow}