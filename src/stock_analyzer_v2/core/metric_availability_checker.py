from distutils.command.install import value

from stock_analyzer_v2.core.yfinance_fetcher import YFinanceFetcher
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.core.models.metric_availability import MetricAvailability


class MetricAvailabilityChecker:
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
                available.add(value)

        return MetricAvailability(
            available=available,
            missing=missing
        )
