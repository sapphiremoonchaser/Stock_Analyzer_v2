from datetime import datetime, timedelta
from typing import (
    Dict,
    Any,
    Optional
)
import yfinance as yf


def get_years_active(
    ticker_info: Dict[str, Any],
) -> str:
    """ Approximate the number of years the stock has been publically traded (using first trade date).
    :param ticker_info:
    :return:
    """
    epoch_key = "firstTradeDataEpochUtc"

    if epoch_key in ticker_info and ticker_info[epoch_key]:
        first_trade = datetime.fromtimestamp(ticker_info[epoch_key])
        return str(datetime.now().year - first_trade.year)

    return "N/A"


def fetch_basic_stock_info(
        ticker_symbol: str
) -> Optional[Dict[str, Any]]:
    """
    Fetch core information for a single ticker using yfinance.
    Returns a clean dict or None if fetch fails.
    :param ticker_symbol:
    :return:
    """
    try:
        # Get the ticker info and uppercase it
        ticker = yf.Ticker(ticker_symbol.upper())
        info = ticker.info

        # If you can't find the ticker or price return None
        if not info or "regularMarketPrice" not in info:
            return None

        # Current price & volume (most recent trading day)
        hist = ticker.history(period="5d") # 5d gives a buffer for non-trading day
        # If not 5 day history, price and volume are None
        if hist.empty:
            current_price = volume = None
        else:
            current_price = round(hist["Close"].iloc[-1], 2)
            volume = int(hist["Volume"].iloc[-1])

        return {
            "ticker": ticker_symbol.upper(),
            "company_name": info.get("longName", "N/A"),
            "current_price": current_price,
            "volume": volume,
            "market_cap": info.get("marketCap"),
            "trailing_pe": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "description": info.get("longBusinessSummary"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "years_active": get_years_active(info)
            # We'll add cash flow later
        }

    except Exception as e:
        print(f"Error fetching {ticker_symbol}: {e}")
        return None