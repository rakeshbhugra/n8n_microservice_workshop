from fastapi import FastAPI
from pydantic import BaseModel
from voice_agent import make_call

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
    # print(f"Received AQI Level: {data.aqi_level}")
    print(data)
    make_call("John Cena", data.aqi_level, data.warning_message)
    return ResponseData(status="success", message="Data processed successfully")

