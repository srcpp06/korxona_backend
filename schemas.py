from pydantic import BaseModel
from decimal import Decimal

# ---------- CLIENT ----------
class ClientCreate(BaseModel):
    company_name: str
    contact_person: str | None = None
    phone: str | None = None
    email: str | None = None
    address: str | None = None

class ClientUpdate(BaseModel):
    company_name: str | None = None
    phone: str | None = None
    email: str | None = None
    address: str | None = None

# ---------- MATERIAL ----------
class MaterialCreate(BaseModel):
    name: str
    type: str | None = None
    unit: str | None = None
    min_stock: Decimal = 0

class MaterialUpdate(MaterialCreate):
    pass

class MaterialInOut(BaseModel):
    material_id: int
    quantity: Decimal

# ---------- PRODUCT ----------
class ProductCreate(BaseModel):
    name: str
    model_code: str | None = None
    size: str | None = None
    color: str | None = None
    client_id: int | None = None
    price: Decimal | None = None

class ProductMaterialCreate(BaseModel):
    material_id: int
    qty_required: Decimal

# ---------- WORKER ----------
class WorkerCreate(BaseModel):
    full_name: str
    position: str | None = None
    salary_type: str
    salary_amount: Decimal
