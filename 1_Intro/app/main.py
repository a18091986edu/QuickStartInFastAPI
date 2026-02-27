from fastapi import FastAPI

from app.config import config
from app.logger import logger

app = FastAPI()


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.url}")
    return {"db_url: {config.db.url}"}


@app.get("/")
async def root():
    return {"message": "Hello World"}
