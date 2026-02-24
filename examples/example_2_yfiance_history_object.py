"""
This is an example of use of yfinance's history object
"""
from turtledemo.penrose import start

import yfinance as yf
from numpy.f2py.crackfortran import endifs

# Create a ticker
aapl = yf.Ticker("AAPL")

# period: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
# interval: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
aapl_historical = aapl.history(
    start='2026-01-01',
    end='2026-02-23',
    interval="1d",
    actions=False
)

x = 1