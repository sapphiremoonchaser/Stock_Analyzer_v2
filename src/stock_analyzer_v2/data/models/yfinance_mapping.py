from pydantic import (
    BaseModel,
    ContentType, ConfigDict,
)
from stock_analyzer_v2.data.enums.yfinance_source import YFinanceSource


class YFinanceMapping(BaseModel):
    source: YFinanceSource # Where to fetch from
    field: str # exact yfinance key/column
    is_time_series: bool = False # Tells you how to fetch and process

    model_config = ConfigDict(
        frozen=True
    )