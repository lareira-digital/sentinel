from fastapi import FastAPI
from immudb import ImmudbClient, PersistentRootService

from .models import DataIngest, AuditResponse, WrongRequest
from .settings import SentinelSettings

settings = SentinelSettings()
api = FastAPI()

@api.on_event("startup")
async def startup_event():
    dbclient = ImmudbClient(
        ":".join([settings.immudb_host, settings.immudb_port]),
        rs=PersistentRootService())
    dbclient.login(
        username=settings.immudb_user,
        password=settings.immudb_pass
    )
    dbclient.useDatabase(b"sentinel")

api.include_router(data_ingest,
                   prefix="/ingest",
                   tags=["ingest", "data"])

api.include_router(data_query,
                   prefix="/query",
                   tags=["query", "data"])

api.post("/ingest")
async def ingest_data():
    return {"message":"OK"}


api.get("/read")
async def read_data():
    return {"message":"OK"}
