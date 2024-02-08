from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Logging service")


@app.get("/")
async def get_logs():

    result = "not implemented yet"
    logging.info(f"Returned: {result}")
    return result
