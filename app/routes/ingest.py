from fastapi import APIRouter
from starlette import status
from immudb import ImmudbClient

from ..models import AuditResponse, ResponseModel, DataIngest

router = APIRouter()

router.post("Ingest data",
            summary="Record data sent by an emmitter",
            description="Ingest audit data sent by an emmiter and record it"
                        "in the database",
            responses={
                status.HTTP_401_UNAUTHORIZED: {"model": ResponseModel},
                status.HTTP_403_FORBIDDEN: {"model": ResponseModel}
            })
async def save_audit_data(entry: DataIngest):
    # Verify GPG key
