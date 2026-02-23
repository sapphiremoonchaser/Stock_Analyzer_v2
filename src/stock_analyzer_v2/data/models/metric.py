"""
Defines the MetricDefinition model.

This module contains the MetricDefinition class, which provides structured metadata
describing financial metrics used throughout the stock analyzer.

Metric definitions act as a centralized registry of metric attributres including:

    - The metric identifier (a StockMetric object)
    - The metric's category (a MetricCategory object)
    - Whether higher values are preferable
    - Whether the metric is a ratio

This is used in the registries.
"""
from pydantic import (
    BaseModel,
    ConfigDict
)
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.metric_category import MetricCategory


class MetricDefinition(BaseModel):
    """
    Immutable metadata describing a financial metric.

    MetricDefinition defines how a specific StockMetric behaves within the system. It
    provides contextual information used for:

        - Ranking and scoring algorithms
        - Portfolio analysis
        - Reporting and visualization logic
        - Strategy evaluation

    Attributes:
        metric (StockMetric):
            The metric being described.
        category (MetricCategory):
            The classification group of the metric (e.g., valuation, profitability).
        higher_is_better (bool):
            Indicates whether higher values are considered more favorable for
            analysis and scoring.
        is_ratio (bool):
            Specifies whether the metric represents a ration (e.g., pe_ratio,
            pb_ratio). Used for formatting and scoring logic.

    Model Configuration:
        - frozen=True
            Instances are immutable to ensure metric definitions remain consistent
            across the application.
        - use_enum_values=True
            Enum values are serialized as their raw values for compatibility with
            JSON and external systems.
    """
    metric: StockMetric
    category: MetricCategory
    higher_is_better: bool
    is_ratio: bool = True

    model_config = ConfigDict(
        frozen=True, # Metrics shouldn't mutate
        use_enum_values=True
    )
