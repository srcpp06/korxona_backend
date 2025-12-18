from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Client, Material


async def get_clients(db: AsyncSession):
    result = await db.execute(select(Client))
    return result.scalars().all()


async def get_materials(db: AsyncSession):
    result = await db.execute(select(Material))
    return result.scalars().all()
