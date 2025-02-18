import logging
import asyncio
from fastapi import FastAPI
from application.core.log_conf import logging_config
from application.routes.user_routes import router as users_router
from application.core.load_data import load_data

app = FastAPI()
app.include_router(users_router)
logging_config()
logger = logging.getLogger(__name__)


async def main():
    logging.info("update database")
    await load_data()


if __name__ == "__main__":
    # uvicorn application.main:app --reload
    asyncio.run(main())
    import uvicorn

    logging.info("start application")
    uvicorn.run(app, host="127.0.0.1", port=8000)
