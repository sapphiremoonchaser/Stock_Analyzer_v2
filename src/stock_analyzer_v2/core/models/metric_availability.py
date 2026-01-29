from pydantic import BaseModel
from stock_analyzer_v2.data.enums.metrics import StockMetric


class MetricAvailability(BaseModel):
    available: set[StockMetric]
    missing: set[StockMetric]
