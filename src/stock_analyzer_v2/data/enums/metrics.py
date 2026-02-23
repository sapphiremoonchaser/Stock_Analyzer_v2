"""
Defines the StockMetric enumeration used throughout the stock analyzer project.

StockMetric provides a standardized set of metrics. Update this when adding new metrics.
"""
from enum import Enum


class StockMetric(Enum):
    """Enumeration for metrics used in the stock analyzer."""
    pe_ratio = 'pe_ratio'
    ev_to_ebitda = 'ev_to_ebitda'
    free_cash_flow = 'free_cash_flow'
    revenue = 'revenue'
