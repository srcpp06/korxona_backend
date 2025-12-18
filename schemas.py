from pydantic import BaseModel

class ClientCreate(BaseModel):
    company_name: str
    phone: str | None = None

class ClientOut(ClientCreate):
    id: int
    class Config:
        from_attributes = True

class MaterialCreate(BaseModel):
    name: str
    unit: str | None = None

class MaterialOut(MaterialCreate):
    id: int
    class Config:
        from_attributes = True
