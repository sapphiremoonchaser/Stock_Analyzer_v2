# Stock_Analyzer_v2

### Adding Metrics

1. Add the metric name to `stock_analyzer_v2/data/enums/metrics.py`
2. If it is a new metric category, add the category to `stock_analyzer_v2/data/enums/metric_category.py`
3. Add to Metric Registry, `stock_analyzer_v2/data/registries/metric_registry.py`
4. If it's a new yfinance source add to `stock_analyzer_v2/data/enums/yfinance_source.py`
5. Add to YFINANCE_METRIC_MAP, `stock_analyzer_v2/data/registries/yfinance_metric_map.py`

