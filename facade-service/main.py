from fastapi import FastAPI
from .models import Message
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Facade service")


@app.get("/")
async def get_messages():
    return "Restaurant order taker"

@app.post("/")
async def post_message(message: Message):
    return "Restaurant order taker"