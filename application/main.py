from fastapi import FastAPI
from application.routes.user_routes import router as users_router

app = FastAPI()
app.include_router(users_router)

if __name__ == "__main__":
    # python3 -m application.main
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
