from fastapi import FastAPI, HTTPException
from .models import Message, PostMessage
import logging
import requests
import uuid

messages_service_url = "http://messages-service:8080/"
logging_service_url = "http://logging-service:8080/"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Facade service")


@app.get("/")
async def get_messages():
    try:
        messages_response = requests.get(messages_service_url)
        messages_response.raise_for_status()
        messages_data = messages_response.json()

        logging_response = requests.get(logging_service_url)
        logging_response.raise_for_status()
        logging_data = logging_response.json()

        combined_data = {
            "messages": messages_data,
            "logging": logging_data
        }
        logging.info(f"Returned data: {str(combined_data)}")
        return combined_data

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to sent get request from facade: {e}")
        raise HTTPException(status_code=500, detail="Failed to sent get request")

@app.post("/")
async def post_message(message: Message):
    logging.info(f"Got message: {str(message)}")
    id = str(uuid.uuid4())
    data = PostMessage(id=id, text=message.text)

    try:
        logging.info(f"Posting message: {str(data)}")
        response = requests.post(messages_service_url, json=data.dict())
        response.raise_for_status()
        logging.info(f"Message posted successfully")
        return {"message": "Message posted successfully"}
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to post message: {e}")
        raise HTTPException(status_code=500, detail="Failed to post message to messages service")
