from typing import List

from fastapi import FastAPI
import logging
from .models import Message
import hazelcast
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Logging service")

hazelcast_cluster_member = os.getenv("HAZELCAST_CLUSTER_MEMBER", "localhost:5701")

client = hazelcast.HazelcastClient(
    cluster_members=[
        hazelcast_cluster_member
    ],
    cluster_name="hazel_claster"
)

distributed_map = client.get_map("distributed_map").blocking()

@app.get("/", response_model=List[str])
async def get_messages():

    result = distributed_map.values()
    print(result)
    logging.info(f"Returned: {result}")
    return result

@app.post("/")
async def post_message(message: Message):

    logging.info(f"Got message with: {str(message)}")
    distributed_map.set(message.id, message.text)
    result = 200
    logging.info(f"Returned: {result}")
    return result
