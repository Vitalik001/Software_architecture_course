from fastapi import FastAPI
import logging
import pika
from threading import Thread
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Messages service")

messages = []


def rabbitmq_consumer():
    global messages
    time.sleep(15) # wait for rabbit mq
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='message_queue')

    def callback(ch, method, properties, body):
        global messages
        messages.append(body.decode())
        logging.info(f"Received message: {body.decode()}")
        logging.info(f"messages: {messages}")

    channel.basic_consume(queue='message_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


@app.on_event("startup")
async def startup_event():
    # Start the RabbitMQ consumer in a background thread
    thread = Thread(target=rabbitmq_consumer)
    thread.start()


@app.get("/")
async def get_messages():
    global messages
    logging.info(f"Returned messages: {messages}")
    return messages
