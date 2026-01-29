from collections.abc import mappingproxy
from typing import Any

import yfinance as yf
import pandas as pd

from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.yfinance_source import YFinanceSource
from stock_analyzer_v2.data.registries.yfinance_metric_map import YFINANCE_METRIC_MAP

class YFinanceFetcher:
    def __init__(
            self,
            ticker: str
    ):
        self.ticker_symbol = ticker
        self.ticker = yf.Ticker(ticker)

    # Helper function for fetch_data()
    def _from_info(
        self,
        field:str
    ) -> Any | None:
        """
        This is a helper function for fetch_data().
        A field is given that will match yfinance. Ex: marketCap instead of market_cap)
        Data is then pulled via yfinance's info() for that field.
        :param field: ticker you need to pull info from
        :return: info object for the given field
        """
        return self.ticker.info.get(field)

    def _from_dataframe(
        self,
        df: pd.DataFrame,
        field:str,
        is_time_series: bool
    ) -> Any | None:
        """
        This is a helper function that looks through a dataframe to return info.
        If the dataframe is None, empty, or the field cannot be found in the index,
        None is returned. If it does find the field it takes that row as a series.
        :param df: dataframe to look through
        :param field: field needed (ex marketCap)
        :param is_time_series:
        :return:
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
        metric: StockMetric,
        source: YFinanceSource,
    ) -> Any | None:
        """
        Fetch a raw metric value or time series from yfinance.
        Returns None if data is missing.
        :param metric:
        :param source:
        """
        mapping = YFINANCE_METRIC_MAP.get(metric)

        if not mapping:
            raise ValueError(f"No yfinance mapping for metric: {metric}")

        try:
            if mapping.source == YFinanceSource.info:
                return self._from_info(mapping.field)

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

        except Exception:
            return None

        return None