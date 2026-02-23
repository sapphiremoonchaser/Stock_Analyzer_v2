"""
yfinance data fetcher implementation.

This module provides the YFinanceFetcher class, which is responsible for retrieving
financial metrics from the yfinance library and translating them into values usable
by the stock analyzer system.

The fetcher:

    - Maps internal StockMetric identifiers to yfinance fields
    - Retrieves data from the appropriate yfinance source
    - Handles both scalar values and time-series data
    - Gracefully returns None when data is unavailable

By isolating all yfinance-specific logic in this module, the system maintains a clean
separation between:

    - Domain logic (metrics, scoring, filtering)
    - External data provider integration

This makes the architecture extensible and allows future replacement or addition of
alternative data providers.
"""
from typing import Any
import yfinance as yf
import pandas as pd

from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.yfinance_source import YFinanceSource
from stock_analyzer_v2.data.registries.yfinance_metric_map import YFINANCE_METRIC_MAP

class YFinanceFetcher:
    """
    Retrieves financial metric data from yfinance for a given ticker.

    YFinanceFetcher acts as the infrastructure layer responsible for translating
    internal StockMetric identifiers into concrete yfinance API calls. It uses the
    YFINANCE_METRIC_MAP registry to determine:

        - Which yfinance source to query (info, financials, cash flow, etc.)
        - The exact field/key to extract
        - Whether special time-series handling is required

    The class returns raw values or pandas Series objects depending on the metric
    configuration. Missing or unavailable data is returned as None.

    Args:
        ticker (str):
            The stock ticker symbol (e.g., "AAPL")

    Design Notes:

        - All provider-specific logic is encapsulated in this class.
        - Failures are handled gracefully to avoid breaking higher layers.
        - Designed to be replaceable with alternative data providers.
    """
    def __init__(
            self,
            ticker: yf.Ticker,
    ):
        self.ticker_symbol = ticker
        self.ticker = yf.Ticker(ticker)

    # Helper function for fetch_data()
    def _from_info(
        self,
        field:str
    ) -> Any | None:
        """
        Retrieve a scalar value from yfinance's 'info' endpoint.

        This helper function extracts a single field from the ticker's 'info'
        dictionary. It returns None if the field is unavailable.

        Args:
            field (str):
                The exact yfinance key (e.g., "marketCap")

        Returns:
            Any | None
                The raw value is available, otherwise None.
        """
        return self.ticker.info.get(field)

    def _from_dataframe(
        self,
        df: pd.DataFrame,
        field:str,
        is_time_series: bool
    ) -> Any | None:
        """
        Retrieve a value or time series from a yfinance DataFrame source.

        This helper function searches for the requested field within the DataFrame
        index (row labels). If found:

            - Returns a sorted pandas Series when 'is_time_series' is True.
            - Returns the most recent value when is_time_series is False.

        Args:
            df (pd.DataFrame):
                The DataFrame returned by yfinance (e.g., financials, cash flow)
            field (str):
                The exact row label to extract.
            is_time_series (bool):
                Whether the metric should be returned as a full time series instead
                of a single value

        Returns:
            Any | None
                A pandas Series, scalar value, or None if unavailable.
        """
        if df is None or df.empty:
            return None

        if field not in df.index:
            return None

        series = df.loc[field]

        if is_time_series:
            return series.sort_index()

        # Most recent value
        return series.iloc[0]


    def fetch_metric(
        self,
        metric: StockMetric
    ) -> Any | None:
        """
        Fetch a metric from yfinance based on its internal definition.

        This method:

            1. Looks up the metric in YFINANCE_METRIC_MAP.
            2. Determines the appropriate yfinance source.
            3. Delegates retrieval to the appropriate helper method.
            4. Returns None if data is missing or an error occurs.

        Args:
            metric (StockMetric):
                The internal metric identifier to retrieve.

        Returns:
            Any | None
                :arg scalar value or pandas Series depending on the metric
                configuration, or None if unavailable.

        Raises:
            ValueError:
                If the metric is not mapped in YFINANCE_METRIC_MAP.
        """
        # Get the correct yfinance source and field
        mapping = YFINANCE_METRIC_MAP.get(metric)

        # Return a Value Error if the metric can't be mapped
        if not mapping:
            raise ValueError(f"No yfinance mapping for metric: {metric}")

        # Return the correct info based on the yfinance source
        try:
            # If source is 'info' use the _from_info helper function
            if mapping.source == YFinanceSource.info:
                return self._from_info(mapping.field)

            # Use the _from_dataframe helper function for all other sources
            if mapping.source == YFinanceSource.financials:
                return self._from_dataframe(
                    self.ticker.financials,
                    mapping.field,
                    mapping.is_time_series,
                )

            if mapping.source == YFinanceSource.cash_flow:
                return self._from_dataframe(
                    self.ticker.cash_flow,
                    mapping.field,
                    mapping.is_time_series
                )

            if mapping.source == YFinanceSource.balance_sheet:
                return self._from_dataframe(
                    self.ticker.balance_sheet,
                    mapping.field,
                    mapping.is_time_series
                )

        except (KeyError, IndexError, AttributeError):
            return None

        return None