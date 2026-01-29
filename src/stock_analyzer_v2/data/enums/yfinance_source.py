from enum import Enum


class YFinanceSource(str, Enum):
    info = "info"
    financials = "financials"
    cash_flow = "cash_flow"
    balance_sheet = "balance_sheet"
    price_history = "price_history"
