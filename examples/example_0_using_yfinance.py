import yfinance as yf
from numpy.ma.core import append

# Get Ticker object
aapl = yf.Ticker("AAPL")

# Get info
info = aapl.info
info_columns = info.keys()

# Get cash flow
cash_flow = aapl.cash_flow
cash_flow_columns = cash_flow.index

# Get financials
financials = aapl.financials
financials_columns = financials.index

# Get balance sheet
balance_sheet = aapl.balance_sheet
balance_sheet_columns = balance_sheet.index

# Get income_stmt
income_statement = aapl.income_stmt
income_statement_columns = income_statement.index

x = 1