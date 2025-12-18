from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
import crud, schemas

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/clients", response_model=schemas.ClientOut)
async def add_client(data: schemas.ClientCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_client(db, data)

@router.get("/clients", response_model=list[schemas.ClientOut])
async def list_clients(db: AsyncSession = Depends(get_db)):
    return await crud.get_clients(db)
