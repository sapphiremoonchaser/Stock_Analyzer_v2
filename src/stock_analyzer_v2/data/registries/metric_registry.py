"""
Central registry of supported financial metrics.

This module defines the METRICS dictionary, which serves as the authoritative
configuration for all metrics recognized by the system.

Each entry maps a StockMetric to its corresponding MetricDefinition, which describes:

    - The metric's category (e.g., valuation, cash flow)
    - Whether higher values are preferable
    - Whether the metric represents a ratio

The registry is used by:

    - Filtering logic (to validate supported metrics)
    - Scoring engines (to determine ranking)
    - UI schema generation (to group and display metrics properly)
    - Reporting components

By centralizing metric configuration here, the system avoids hardcoded logic
scattered across services and ensures consistent behavior across filtering, scoring,
and presentation layers.
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
    ),

    StockMetric.revenue: MetricDefinition(
        metric=StockMetric.revenue,
        category=MetricCategory.cash_flow,
        higher_is_better=True,
        is_ratio=False
    )
}