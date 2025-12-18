from fastapi import FastAPI
from routers import router

app = FastAPI(
    title="Production Management Backend",
    version="1.0"
)

app.include_router(router)
