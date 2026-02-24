"""
This is an example of how to get the current price of a stock.
"""
import yfinance as yf
from examples.example_0_using_yfinance import info

# Create the ticker
aapl = yf.Ticker("AAPL")

# Get info
info = aapl.info

# Get current price


x = 1