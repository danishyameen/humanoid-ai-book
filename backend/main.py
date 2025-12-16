from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend!"}