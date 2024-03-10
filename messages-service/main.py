from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Messages service")


@app.get("/")
async def get_messages():

    result = "not implemented yet"
    logging.info(f"Returned: {result}")
    return result
