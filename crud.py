from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from . import models

# =====================================================
# CLIENT CRUD
# =====================================================

def create_client(db: Session, data: dict):
    client = models.Client(**data)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


def get_clients(db: Session):
    return db.query(models.Client).all()


def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def update_client(db: Session, client_id: int, data: dict):
    client = get_client(db, client_id)
    if not client:
        return None

    for key, value in data.items():
        setattr(client, key, value)

    db.commit()
    db.refresh(client)
    return client


def delete_client(db: Session, client_id: int):
    client = get_client(db, client_id)
    if not client:
        return False

    db.delete(client)
    db.commit()
    return True


# =====================================================
# MATERIAL CRUD
# =====================================================

def create_material(db: Session, data: dict):
    material = models.Material(**data)
    db.add(material)
    db.commit()
    db.refresh(material)

    # stock avtomatik ochiladi
    stock = models.MaterialStock(
        material_id=material.id,
        quantity=0
    )
    db.add(stock)
    db.commit()

    return material


def get_materials(db: Session):
    return db.query(models.Material).all()


def get_material(db: Session, material_id: int):
    return db.query(models.Material).filter(
        models.Material.id == material_id
    ).first()


def update_material(db: Session, material_id: int, data: dict):
    material = get_material(db, material_id)
    if not material:
        return None

    for key, value in data.items():
        setattr(material, key, value)

    db.commit()
    db.refresh(material)
    return material


def delete_material(db: Session, material_id: int):
    material = get_material(db, material_id)
    if not material:
        return False

    db.delete(material)
    db.commit()
    return True


# =====================================================
# MATERIAL STOCK + LOGS
# =====================================================

def update_material_stock(
    db: Session,
    material_id: int,
    change_qty: float,
    reason: str
):
    stock = db.query(models.MaterialStock).filter(
        models.MaterialStock.material_id == material_id
    ).first()

    if not stock:
        return None

    stock.quantity += change_qty

    log = models.MaterialLog(
        material_id=material_id,
        change_qty=change_qty,
        reason=reason
    )

    db.add(log)
    db.commit()
    db.refresh(stock)

    return stock


def get_low_stock_materials(db: Session):
    return (
        db.query(models.Material)
        .join(models.MaterialStock)
        .filter(models.MaterialStock.quantity < models.Material.min_stock)
        .all()
    )


# =====================================================
# WORKER CRUD
# =====================================================

def create_worker(db: Session, data: dict):
    worker = models.Worker(**data)
    db.add(worker)
    db.commit()
    db.refresh(worker)
    return worker


def get_workers(db: Session):
    return db.query(models.Worker).all()


def get_worker(db: Session, worker_id: int):
    return db.query(models.Worker).filter(
        models.Worker.id == worker_id
    ).first()


def update_worker(db: Session, worker_id: int, data: dict):
    worker = get_worker(db, worker_id)
    if not worker:
        return None

    for key, value in data.items():
        setattr(worker, key, value)

    db.commit()
    db.refresh(worker)
    return worker


def delete_worker(db: Session, worker_id: int):
    worker = get_worker(db, worker_id)
    if not worker:
        return False

    db.delete(worker)
    db.commit()
    return True


# =====================================================
# PRODUCT CRUD
# =====================================================

def create_product(db: Session, data: dict):
    product = models.Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()


def update_product(db: Session, product_id: int, data: dict):
    product = get_product(db, product_id)
    if not product:
        return None

    for key, value in data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if not product:
        return False

    db.delete(product)
    db.commit()
    return True


# =====================================================
# PRODUCT MATERIALS
# =====================================================

def add_material_to_product(
    db: Session,
    product_id: int,
    material_id: int,
    qty_required: float
):
    pm = models.ProductMaterial(
        product_id=product_id,
        material_id=material_id,
        qty_required=qty_required
    )
    db.add(pm)
    db.commit()
    return pm


def get_product_materials(db: Session, product_id: int):
    return db.query(models.ProductMaterial).filter(
        models.ProductMaterial.product_id == product_id
    ).all()


# =====================================================
# WORK LOGS
# =====================================================

def add_work_log(
    db: Session,
    worker_id: int,
    product_id: int,
    quantity: int,
    work_date: date
):
    log = models.WorkLog(
        worker_id=worker_id,
        product_id=product_id,
        quantity=quantity,
        work_date=work_date
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_worker_production(db: Session):
    return (
        db.query(
            models.Worker.full_name,
            func.sum(models.WorkLog.quantity).label("total")
        )
        .join(models.WorkLog)
        .group_by(models.Worker.id)
        .all()
    )
