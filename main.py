from fastapi import FastAPI
from routers import router
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Production Backend")

app.include_router(router)
