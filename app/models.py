"""Data models for ingestion and extraction.

- Why use datetime.date? to avoid Y2K38 more info here:
  https://en.wikipedia.org/wiki/Year_2038_problem
"""

from datetime import datetime

from typing import List, Union, Optional
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


class ResponseModel(BaseModel):
    status: str = Field(
        None,
        alias="Status",
        title="Status of the request",
        description="Status of the request (success, fail or error)"
    )
    message: Optional[str] = Field(
        None,
        alias="Message",
        title="Informational Message",
        description="Mesage describing what happened to the request"
    )
    data: Optional[str] = Field(
        None,
        alias="Data",
        title="Request data",
        description="Data that failed during the request"
    )
