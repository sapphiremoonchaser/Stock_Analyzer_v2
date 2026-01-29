from stock_analyzer_v2.data.registries.yfinance_metric_map import YFINANCE_METRIC_MAP
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.yfinance_source import YFinanceSource


def test_pe_ratio_mapping():
    mapping = YFINANCE_METRIC_MAP[StockMetric.pe_ratio]

    # Check for correct attributes
    assert mapping.source == YFinanceSource.info
    assert mapping.field == 'trailingPE'
    assert mapping.is_time_series is False

