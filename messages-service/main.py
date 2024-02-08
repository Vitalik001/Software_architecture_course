from typing import List

from fastapi import FastAPI
import logging
from .models import Message


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Messages service")

messages_db = {}

@app.get("/", response_model=List[str])
async def get_messages():

    result = list(messages_db.values())
    logging.info(f"Returned: {result}")
    return result

@app.post("/")
async def post_message(message: Message):

    logging.info(f"Got message with: {str(message)}")
    messages_db[message.id] = message.text
    result = 200
    logging.info(f"Returned: {result}")
    return result
