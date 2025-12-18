from sqlalchemy import (
    Column, Integer, String, ForeignKey,
    Date, Enum, DECIMAL, TIMESTAMP
)
from database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    company_name = Column(String(150), nullable=False)
    contact_person = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(String(255))
    created_at = Column(TIMESTAMP)

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50))
    unit = Column(String(20))
    min_stock = Column(DECIMAL(10, 2))

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    position = Column(String(50))
    phone = Column(String(20))
    salary_type = Column(Enum("oylik", "dona"))
    salary_amount = Column(DECIMAL(10, 2))
    hired_date = Column(Date)
    active = Column(Integer, default=1)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model_code = Column(String(50))
    size = Column(String(20))
    color = Column(String(30))
    client_id = Column(Integer, ForeignKey("clients.id"))
    price = Column(DECIMAL(10, 2))
