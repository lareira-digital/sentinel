from fastapi import FastAPI

api = FastAPI()


app.post("/ingest")


async def ingest_data():
    pass


app.get("/read", response_model=AuditResponse)


async def read_data():
    pass
