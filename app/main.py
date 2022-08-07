from fastapi import FastAPI

api = FastAPI()


api.post("/ingest")


async def ingest_data():
    pass


api.get("/read", response_model=AuditResponse)


async def read_data():
    pass
