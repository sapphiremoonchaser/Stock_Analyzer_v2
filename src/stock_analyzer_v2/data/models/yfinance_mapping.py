"""
Defines field mappings between internal metrics and yfinance data sources.

This module contains the YFinanceMapping model, which describes how a financial
metric should be retrieved from yfinance. It specifies:

    - The source endpoint within yfinance
    - The exact field/key name to extract
    - Whether the data represents a time series

By centralizing this mapping logic, the system avoids hardcoding API field names
throughout the codebase and maintains a clear separation between internal domain
models (StockMetric, MetricDefinition) and external data provider (yfinance schema).
"""
from pydantic import (
    BaseModel,
    ConfigDict
)
from stock_analyzer_v2.data.enums.yfinance_source import YFinanceSource


class YFinanceFieldMapping(BaseModel):
    """
    Immutable configuration describing how to fetch a metric from yfinance.

    YFinanceFieldMapping defines the connection between an internal metric and its
    corresponding representation in yfinance. It provides enough information for a
    fetcher service to determine:

        - Which yfinance data source to query
        - Which field/key to extract from the response
        - Whether special handling is required for time-series data

    Attributes:
        source (YFinanceSource):
            The yfinance endpoint or data group to retrieve data from (e.g., info,
            financials, balance_sheet).
        field (str):
            The exact key or column name used by yfinance.
        is_time_series (bool):
            Indicates whether the data represents a time series requiring aggregation or
            transformation before use.

    Model Configuration:
        - frozen=True
            Ensures mappings remain immutable and consistent throughout the app.
    """
    source: YFinanceSource # Where to fetch from
    field: str # exact yfinance key/column
    is_time_series: bool = False # Tells you how to fetch and process

    model_config = ConfigDict(
        frozen=True
    )

