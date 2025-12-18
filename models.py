from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    DECIMAL,
    ForeignKey,
    Text,
    Enum,
    Date,
    TIMESTAMP
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .database import Base

# =========================
# CLIENTS
# =========================

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(150), nullable=False)
    contact_person = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(String(255))
    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    products = relationship(
        "Product",
        back_populates="client",
        cascade="all, delete"
    )


# =========================
# MATERIALS
# =========================

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50))
    unit = Column(String(20))
    min_stock = Column(DECIMAL(10, 2), default=0)
    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    stock = relationship(
        "MaterialStock",
        back_populates="material",
        uselist=False,
        cascade="all, delete"
    )

    logs = relationship(
        "MaterialLog",
        back_populates="material",
        cascade="all, delete"
    )


# =========================
# MATERIAL STOCK
# =========================

class MaterialStock(Base):
    __tablename__ = "material_stock"

    material_id = Column(
        Integer,
        ForeignKey("materials.id", ondelete="CASCADE"),
        primary_key=True
    )
    quantity = Column(DECIMAL(10, 2), nullable=False, default=0)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )

    material = relationship(
        "Material",
        back_populates="stock"
    )


# =========================
# MATERIAL LOGS
# =========================

class MaterialLog(Base):
    __tablename__ = "material_logs"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(
        Integer,
        ForeignKey("materials.id", ondelete="CASCADE"),
        nullable=False
    )
    change_qty = Column(DECIMAL(10, 2), nullable=False)
    reason = Column(
        Enum("kirim", "chiqim", "ishlab_chiqarish"),
        nullable=False
    )
    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    material = relationship(
        "Material",
        back_populates="logs"
    )


# =========================
# WORKERS
# =========================

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    position = Column(String(50))
    phone = Column(String(20))
    salary_type = Column(
        Enum("oylik", "dona"),
        nullable=False
    )
    salary_amount = Column(DECIMAL(10, 2))
    hired_date = Column(Date)
    active = Column(Integer, default=1)

    work_logs = relationship(
        "WorkLog",
        back_populates="worker",
        cascade="all, delete"
    )


# =========================
# PRODUCTS
# =========================

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    model_code = Column(String(50))
    size = Column(String(20))
    color = Column(String(30))
    client_id = Column(
        Integer,
        ForeignKey("clients.id", ondelete="SET NULL")
    )
    price = Column(DECIMAL(10, 2))
    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    client = relationship(
        "Client",
        back_populates="products"
    )

    materials = relationship(
        "ProductMaterial",
        back_populates="product",
        cascade="all, delete"
    )

    work_logs = relationship(
        "WorkLog",
        back_populates="product",
        cascade="all, delete"
    )


# =========================
# PRODUCT MATERIALS
# =========================

class ProductMaterial(Base):
    __tablename__ = "product_materials"

    product_id = Column(
        Integer,
        ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True
    )
    material_id = Column(
        Integer,
        ForeignKey("materials.id", ondelete="CASCADE"),
        primary_key=True
    )
    qty_required = Column(DECIMAL(10, 2), nullable=False)

    product = relationship(
        "Product",
        back_populates="materials"
    )

    material = relationship("Material")


# =========================
# WORK LOGS
# =========================

class WorkLog(Base):
    __tablename__ = "work_logs"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(
        Integer,
        ForeignKey("workers.id", ondelete="CASCADE"),
        nullable=False
    )
    product_id = Column(
        Integer,
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False
    )
    quantity = Column(Integer, nullable=False)
    work_date = Column(Date, nullable=False)

    worker = relationship(
        "Worker",
        back_populates="work_logs"
    )

    product = relationship(
        "Product",
        back_populates="work_logs"
    )
