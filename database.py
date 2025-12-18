import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = os.getenv("mysql+aiomysql://root:VpwfzwEsoyVyWmWzBOuLNodFpfmChcqJ@switchyard.proxy.rlwy.net:26735/railway")

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with SessionLocal() as session:
        yield session
