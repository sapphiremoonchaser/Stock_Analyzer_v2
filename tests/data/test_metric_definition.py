from stock_analyzer_v2.data.registries.metric_registry import METRICS
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.metric_category import MetricCategory


def test_metric_definition_metadata():
    fcf = METRICS[StockMetric.free_cash_flow]

    # Correct metric category and attributes
    assert fcf.category == MetricCategory.cash_flow
    assert fcf.higher_is_better is True
    assert fcf.is_ratio is False
