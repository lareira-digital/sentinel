from fastapi import FastAPI

api = FastAPI()

app.get("/")
async def root():
    return {"message": "Hello world"}
