import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine.url import make_url

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
# =========================
# DATABASE URL
# =========================

if not DATABASE_URL:
    raise RuntimeError("❌ DATABASE_URL topilmadi (Railway env o‘rnatilmagan)")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,      # uzilgan connectionlarni tekshiradi
    pool_recycle=1800,       # Railway timeout muammosi uchun
    echo=False               # True qilsang SQL log chiqadi
)

# =========================
# SESSION
# =========================

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

# =========================
# BASE
# =========================

Base = declarative_base()

# =========================
# DEPENDENCY
# =========================

def get_db():
    """
    FastAPI dependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
