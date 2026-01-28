from enum import Enum


class MetricCategory(str, Enum):
    valuation = 'valuation'
    cash_flow = 'cash_flow'
    growth = 'growth'
    profitability = 'profitability'
