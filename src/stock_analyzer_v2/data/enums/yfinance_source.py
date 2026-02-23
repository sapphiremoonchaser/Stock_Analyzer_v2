"""
Defines the YFinanceSource enumeration used throughout the stock analyzer project.

YFinanceSource provides a standardized set of yfiance data sources. For example,
'sector' would come from 'info' whereas 'operating_cash_flow' would come from
yfinance's 'cashflow' object.
"""
from enum import Enum


class YFinanceSource(str, Enum):
    """Enumeration for YFinanceSource used in the stock analyzer."""
    info = "info"
    financials = "financials"
    cash_flow = "cash_flow"
    balance_sheet = "balance_sheet"
    price_history = "price_history"
