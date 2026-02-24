from stock_analyzer_v2.core.yfinance_fetcher import YFinanceFetcher
from stock_analyzer_v2.data.enums.metrics import StockMetric

ticker_symbol = 'AAPL'
fetcher = YFinanceFetcher(ticker_symbol)

# Fetch pe_ratio
pe_ratio = fetcher.fetch_metric(StockMetric.pe_ratio)

# Fetch eb_to_ebidta
ev_to_ebidta = fetcher.fetch_metric(StockMetric.ev_to_ebitda)

# Fetch revenue
# revenue[-1:] for most recent
revenue = fetcher.fetch_metric(StockMetric.revenue)

# Fetch free cash flow
fcf = fetcher.fetch_metric(StockMetric.free_cash_flow)

x = 1