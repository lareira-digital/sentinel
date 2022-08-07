"""Data models for ingestion and extraction.

- Why use datetime.date? to avoid Y2K38 more info here:
  https://en.wikipedia.org/wiki/Year_2038_problem
"""

from datetime import datetime

from typing import List, Union
from pydantic import BaseModel, Field


class CommonData(BaseModel)
    emitter: str = Field(
        ...,
        alias="Emmiter",
        title="Emitter",
        description="Service sending the data",
    )
    message: str = Field(
        ...,
        alias="Message",
        title="Message",
        description="Message of the audit"
    )
    timestamp: datetime.date = Field(
        ...,
        alias="Message datetime",
        title="Message datetime",
        description="What time, date and timezone the message was received"
    )
    extra_data: str = Field(
        None,
        alias="Extra data",
        title="Extra data",
        description="Extra data send by the emmiter"
    )


class DataIngest(CommonData):
    signed_message: bool = Field(
        None,
        alias="Signed message",
        title="Signed message",
        description="Mark the message as cryptographically signed"
    )


class AuditResponse(BaseModel):
    entries: List[CommonResponse]


class WrongRequest(BaseModel):
    error: str
    message: str
