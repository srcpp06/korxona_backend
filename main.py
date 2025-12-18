from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from . import models
from .routers import router as api_router

# =========================
# CREATE TABLES
# =========================
# Eslatma:
# Agar Railway MySQL’da jadval allaqachon mavjud bo‘lsa
# bu qator hech narsa buzmaydi

models.Base.metadata.create_all(bind=engine)

# =========================
# APP
# =========================

app = FastAPI(
    title="Factory Management Backend",
    description="Client, Material, Product, Worker va Ombor boshqaruvi",
    version="1.0.0"
)

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # keyin frontend domen bilan cheklaysan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROUTERS
# =========================

app.include_router(api_router)

# =========================
# ROOT
# =========================

@app.get("/")
def root():
    return {
        "status": "OK",
        "message": "Backend ishlayapti 🚀"
    }
