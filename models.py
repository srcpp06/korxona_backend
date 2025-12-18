from sqlalchemy import (
    Column, Integer, String, Date, DECIMAL,
    ForeignKey, Enum, TIMESTAMP
)
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    company_name = Column(String(150), nullable=False)
    contact_person = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    products = relationship("Product", back_populates="client")


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50))
    unit = Column(String(20))
    min_stock = Column(DECIMAL(10,2), default=0)

    stock = relationship("MaterialStock", uselist=False)
    logs = relationship("MaterialLog")


class MaterialStock(Base):
    __tablename__ = "material_stock"

    material_id = Column(Integer, ForeignKey("materials.id"), primary_key=True)
    quantity = Column(DECIMAL(10,2), default=0)

    material = relationship("Material")


class MaterialLog(Base):
    __tablename__ = "material_logs"

    id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey("materials.id"))
    change_qty = Column(DECIMAL(10,2))
    reason = Column(Enum("kirim","chiqim","ishlab_chiqarish"))


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    position = Column(String(50))
    salary_type = Column(Enum("oylik","dona"))
    salary_amount = Column(DECIMAL(10,2))
    active = Column(Integer, default=1)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    client_id = Column(Integer, ForeignKey("clients.id"))
    price = Column(DECIMAL(10,2))

    client = relationship("Client", back_populates="products")
