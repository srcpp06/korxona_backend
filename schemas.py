from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime
from decimal import Decimal

from app.database import engine
from app import models

# =========================
# CLIENT
# =========================

class ClientBase(BaseModel):
    company_name: str = Field(..., max_length=150)
    contact_person: Optional[str] = Field(None, max_length=100)
    phone: Optional[str] = Field(None, max_length=20)
    email: Optional[str] = Field(None, max_length=100)
    address: Optional[str] = Field(None, max_length=255)


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    pass


class ClientOut(ClientBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# MATERIAL
# =========================

class MaterialBase(BaseModel):
    name: str = Field(..., max_length=100)
    type: Optional[str] = Field(None, max_length=50)
    unit: Optional[str] = Field(None, max_length=20)
    min_stock: Decimal = Decimal("0.00")


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(MaterialBase):
    pass


class MaterialOut(MaterialBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# MATERIAL STOCK
# =========================

class MaterialStockOut(BaseModel):
    material_id: int
    quantity: Decimal
    updated_at: datetime

    class Config:
        from_attributes = True


# =========================
# MATERIAL LOGS
# =========================

class MaterialLogOut(BaseModel):
    id: int
    material_id: int
    change_qty: Decimal
    reason: str
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# WORKER
# =========================

class WorkerBase(BaseModel):
    full_name: str = Field(..., max_length=100)
    position: Optional[str] = Field(None, max_length=50)
    phone: Optional[str] = Field(None, max_length=20)
    salary_type: str
    salary_amount: Optional[Decimal]
    hired_date: Optional[date]
    active: Optional[int] = 1


class WorkerCreate(WorkerBase):
    pass


class WorkerUpdate(WorkerBase):
    pass


class WorkerOut(WorkerBase):
    id: int

    class Config:
        from_attributes = True


# =========================
# PRODUCT
# =========================

class ProductBase(BaseModel):
    name: str = Field(..., max_length=100)
    model_code: Optional[str] = Field(None, max_length=50)
    size: Optional[str] = Field(None, max_length=20)
    color: Optional[str] = Field(None, max_length=30)
    client_id: Optional[int]
    price: Optional[Decimal]


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# PRODUCT MATERIALS
# =========================

class ProductMaterialCreate(BaseModel):
    material_id: int
    qty_required: Decimal


class ProductMaterialOut(ProductMaterialCreate):
    product_id: int

    class Config:
        from_attributes = True


# =========================
# WORK LOGS
# =========================

class WorkLogCreate(BaseModel):
    worker_id: int
    product_id: int
    quantity: int
    work_date: date


class WorkLogOut(WorkLogCreate):
    id: int

    class Config:
        from_attributes = True


# =========================
# REPORT SCHEMAS
# =========================

class WorkerProductionOut(BaseModel):
    full_name: str
    total: int
