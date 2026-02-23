from stock_analyzer_v2.data.registries.yfinance_metric_map import YFINANCE_METRIC_MAP
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.yfinance_source import YFinanceSource


def test_pe_ratio_mapping():
    mapping = YFINANCE_METRIC_MAP[StockMetric.pe_ratio]

    # Check for correct attributes
    assert mapping.source == YFinanceSource.info
    assert mapping.field == 'trailingPE'
    assert mapping.is_time_series is False


def test_ev_to_ebitda_mapping():
    mapping = YFINANCE_METRIC_MAP[StockMetric.ev_to_ebitda]

    # Check for correct attributes
    assert mapping.source == YFinanceSource.info
    assert mapping.field == 'enterpriseToEbitda'
    assert mapping.is_time_series is False


def test_revenue_mapping():
    mapping = YFINANCE_METRIC_MAP[StockMetric.revenue]

    # Check for correct attributes
    assert mapping.source == YFinanceSource.financials
    assert mapping.field == 'Total Revenue'
    assert mapping.is_time_series is True


def test_free_cash_flow_mapping():
    mapping = YFINANCE_METRIC_MAP[StockMetric.free_cash_flow]

    # Check for correct attributes
    assert mapping.source == YFinanceSource.info
    assert mapping.field == 'freeCashFlow'
    assert mapping.is_time_series is False

