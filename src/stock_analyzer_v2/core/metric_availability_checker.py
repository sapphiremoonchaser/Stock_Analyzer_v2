"""
Provides functionality for validating metric availability.

This module defines the MetricAvailabilityChecker class, which determines whether the
requested metric is available given a stock by attempting to retrieve via yfinance.

The checker separates data retrieval (handed by the fetcher) and availability
validation (handled here).
"""
from stock_analyzer_v2.core.yfinance_fetcher import YFinanceFetcher
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.core.models.metric_availability import MetricAvailability


class MetricAvailabilityChecker:
    """
    Evaluates whether or not requested stock metrics are available. It queries yfinance
    """
    def __init__(
        self,
        fetcher: YFinanceFetcher
    ):
        self.fetcher = fetcher

    def check(
        self,
        metrics: list[StockMetric],
    ) -> MetricAvailability:
        available: set[StockMetric] = set()
        missing: set[StockMetric] = set()

        for metric in metrics:
            value = self.fetcher.fetch_metric(metric)

            if value is None:
                missing.add(metric)
            else:
                available.add(metric)

        return MetricAvailability(
            available=available,
            missing=missing
        )
