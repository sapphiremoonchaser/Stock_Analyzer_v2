from pydantic import (
    BaseModel,
    ConfigDict
)
from stock_analyzer_v2.data.enums.metrics import StockMetric
from stock_analyzer_v2.data.enums.metric_category import MetricCategory


class MetricDefinition(BaseModel):
    metric: StockMetric
    category: MetricCategory
    higher_is_better: bool
    is_ratio: bool = True

    model_config = ConfigDict(
        frozen=True, # Metrics shouldn't mutate
        use_enum_values=True
    )
