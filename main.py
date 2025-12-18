from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app import models
from app.routers import router

# =========================
# APP INIT
# =========================
app = FastAPI(
    title="Production Management API",
    version="1.0.0",
    description="Clients, materials, products, workers management system"
)

# =========================
# CORS (frontend uchun)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # keyin frontend domen bilan cheklaysan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# STARTUP EVENT
# =========================
@app.on_event("startup")
def on_startup():
    # ⚠️ IMPORT VAQTIDA EMAS!
    models.Base.metadata.create_all(bind=engine)

# =========================
# ROUTERS
# =========================
app.include_router(router)

# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is running"}
