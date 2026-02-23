"""
Defines the MetricCategory enumeration used throughout the stock analyzer project.

MetricCategory provides a standardized set of categories of metrics. For example,
pe_ratio would belong to the 'valuation' MetricCategory. Currently, it is only being
used to categorize metrics.
"""
from enum import Enum


class MetricCategory(str, Enum):
    """Enumeration of supported metric categories."""
    valuation = 'valuation'
    cash_flow = 'cash_flow'
    growth = 'growth'
    profitability = 'profitability'
