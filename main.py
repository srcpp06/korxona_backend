from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from database import get_db, engine
from schemas import (
    ClientCreate, ClientOut,
    MaterialCreate, MaterialOut
)
from crud import (
    create_client, get_clients,
    create_material, get_materials
)

app = FastAPI(
    title="Korxona Admin Backend",
    version="1.0.0"
)

@app.get("/")
def health():
    return {"status": "OK", "db": "railway-mysql"}

@app.on_event("startup")
async def startup():
    async with engine.begin():
        pass

# ---- TEST ----
@app.get("/db-test")
async def db_test(db: AsyncSession = Depends(get_db)):
    r = await db.execute(text("SHOW TABLES"))
    return {"tables": [x[0] for x in r.fetchall()]}

# ---- CLIENTS ----
@app.post("/clients", response_model=ClientOut)
async def add_client(
    data: ClientCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_client(db, data)

@app.get("/clients", response_model=list[ClientOut])
async def list_clients(db: AsyncSession = Depends(get_db)):
    return await get_clients(db)

# ---- MATERIALS ----
@app.post("/materials", response_model=MaterialOut)
async def add_material(
    data: MaterialCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_material(db, data)

@app.get("/materials", response_model=list[MaterialOut])
async def list_materials(db: AsyncSession = Depends(get_db)):
    return await get_materials(db)
