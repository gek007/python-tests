from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class Trade(BaseModel):
    """execute a stock with built-in constrains and validations"""

    symbol: str = Field(
        ...,
        description="the stock symbol (e.g. AAPL)",
        min_length=1,
        max_length=5,
    )

    action: Literal["buy", "sell"] = Field(
        ...,
        description="the action to take (buy or sell)",
    )

    shares: int = Field(
        ...,
        ge=1,
        le=1000,
        description="the number of shares to trade",
    )

    price_limit: float | None = Field(
        default=None,
        gt=0,
        lt=1000,
        description="the price limit for the trade",
    )

    @field_validator("symbol")
    @classmethod
    def validate_stock(cls, value: str) -> str:
        """whitelist"""
        valid_symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]
        if value in valid_symbols:
            return value

        raise ValueError("Symbol must be alphabetic")


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILED = "failed"
    BLOCKED = "blocked"


@dataclass
class Task:
    id: str
    status: TaskStatus
    description: str
    created_at: datetime
    updated_at: datetime
    result: dict | None = None
    error: str | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "status": self.status.value,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "result": self.result,
            "error": self.error,
        }


my_dic: dict[str, Task] = {}
my_list: list[Task] = [
    {
        "docs": ["doc1", "doc2", "doc3"],
        "status": TaskStatus.PENDING,
        "uniq": {1, 2, 3, 4},
    }
]

val = {1, 2, 3, 4}
val2: set[int] = {1, 2, 3, 4}
va3: set[int] = ()
