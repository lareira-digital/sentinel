from typing import List, Union
from pydantic import BaseModel


class CommonData(BaseModel)
    emitter: str
    message: str
    timestamp: str
    extra_data: str


class DataIngest(CommonData):
    pass


class AuditResponse(CommonResponse):
    pass


class WrongRequest(BaseModel):
    error: str
    message: str
