from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

class RequestData(BaseModel):
    aqi_level: str
    warning_message: str

class ResponseData(BaseModel):
    status: str
    message: str


@app.post("/webhook", response_model=ResponseData)
async def process_webhook(data: RequestData):
    print(f"Received AQI Level: {data.aqi_level}")
    return ResponseData(status="success", message="Data processed successfully")

