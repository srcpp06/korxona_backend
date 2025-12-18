from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Client, Material

async def create_client(db: AsyncSession, data):
    obj = Client(**data.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def get_clients(db: AsyncSession):
    res = await db.execute(select(Client))
    return res.scalars().all()

async def create_material(db: AsyncSession, data):
    obj = Material(**data.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def get_materials(db: AsyncSession):
    res = await db.execute(select(Material))
    return res.scalars().all()
