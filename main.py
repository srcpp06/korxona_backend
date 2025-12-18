from fastapi import FastAPI, Depends
from database import get_db
from crud import get_clients, get_materials
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "OK", "db": "railway-mysql"}


@app.get("/clients")
async def clients(db: AsyncSession = Depends(get_db)):
    return await get_clients(db)


@app.get("/materials")
async def materials(db: AsyncSession = Depends(get_db)):
    return await get_materials(db)
