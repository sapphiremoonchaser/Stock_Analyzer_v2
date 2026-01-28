"""Enum for StockMetric
"""
from enum import Enum


class StockMetric(Enum):
    pe_ratio = 'pe_ratio'
    ev_to_ebitda = 'ev_to_ebitda'
    free_cash_flow = 'free_cash_flow'
    revenue = 'revenue'
