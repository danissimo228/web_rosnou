import asyncio
from fastapi import FastAPI
from application.routes.user_routes import router as users_router
from application.core.load_data import load_data

app = FastAPI()
app.include_router(users_router)


async def main():
    await load_data()


if __name__ == "__main__":
    # python3 -m application.main
    asyncio.run(main())
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
