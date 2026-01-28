"""Tells us how the metric is fetched
"""
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.yfinance_source import YFinanceSource
from stock_analyzer_v2.data.models.yfinance_mapping import YFinanceFieldMapping

YFINANCE_METRIC_MAP: dict[
    StockMetric, YFinanceFieldMapping
] = {
    StockMetric.pe_ratio: YFinanceFieldMapping(
        source=YFinanceSource.info,
        field="trailingPE"
    ),

    StockMetric.ev_to_ebitda: YFinanceFieldMapping(
        source=YFinanceSource.info,
        field="enterpriseToEbitda"
    ),

    StockMetric.free_cash_flow: YFinanceFieldMapping(
        source=YFinanceSource.info,
        field="freeCashFlow"
    ),

    StockMetric.revenue: YFinanceFieldMapping(
        source=YFinanceSource.financials,
        field="Total Revenue",
        is_time_series=True
    )
}

