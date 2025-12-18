from pydantic import BaseModel
from decimal import Decimal

class ClientCreate(BaseModel):
    company_name: str
    phone: str | None = None

class ClientOut(ClientCreate):
    id: int

    class Config:
        from_attributes = True


class MaterialInOut(BaseModel):
    material_id: int
    quantity: Decimal
    reason: str
