from stock_analyzer_v2.data.registries.metric_registry import METRICS
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.metric_category import MetricCategory


def test_pe_ratio_definition_metadata():
    pe_ratio = METRICS[StockMetric.pe_ratio]

    # Correct pe_ratio category and attributes
    assert pe_ratio.category == MetricCategory.valuation
    assert pe_ratio.higher_is_better is False
    assert pe_ratio.is_ratio is True


def test_ev_to_ebitda_definition_metadata():
    pass


def test_revenue_definition_metadata():
    pass


def test_metric_definition_metadata():
    fcf = METRICS[StockMetric.free_cash_flow]

    # Correct metric category and attributes
    assert fcf.category == MetricCategory.cash_flow
    assert fcf.higher_is_better is True
    assert fcf.is_ratio is False
