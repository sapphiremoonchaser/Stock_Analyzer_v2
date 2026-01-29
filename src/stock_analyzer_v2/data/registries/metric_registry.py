"""This will be used for filtering, scoring, and the UI schema
Tells us what the metric means
"""
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.metric_category import MetricCategory
from stock_analyzer_v2.data.models.metric import MetricDefinition


METRICS: dict[StockMetric, MetricDefinition] = {
    StockMetric.pe_ratio: MetricDefinition(
        metric=StockMetric.pe_ratio,
        category=MetricCategory.valuation,
        higher_is_better=False
    ),

    StockMetric.ev_to_ebitda: MetricDefinition(
        metric=StockMetric.ev_to_ebitda,
        category=MetricCategory.valuation,
        higher_is_better=False
    ),

    StockMetric.free_cash_flow: MetricDefinition(
        metric=StockMetric.free_cash_flow,
        category=MetricCategory.cash_flow,
        higher_is_better=True,
        is_ratio=False
    )
}