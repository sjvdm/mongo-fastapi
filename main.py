from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

app = FastAPI()

# MongoDB connection URL
MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
database = client["mydatabase"]
collection = database["items"]


@app.get("/")
async def main_route():
    return {"message": "Hey, It is me Goku"}
