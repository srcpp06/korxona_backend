from sqlalchemy.orm import Session
import models

# -------- CLIENT --------
def create_client(db: Session, data):
    obj = models.Client(**data.dict())
    db.add(obj)
    db.commit()
    return obj

def update_client(db, id, data):
    obj = db.get(models.Client, id)
    for k,v in data.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    return obj

# -------- MATERIAL --------
def create_material(db, data):
    m = models.Material(**data.dict())
    db.add(m)
    db.commit()
    db.add(models.MaterialStock(material_id=m.id, quantity=0))
    db.commit()
    return m

def material_in(db, material_id, qty, reason):
    stock = db.get(models.MaterialStock, material_id)
    stock.quantity += qty
    db.add(models.MaterialLog(
        material_id=material_id,
        change_qty=qty,
        reason=reason
    ))
    db.commit()

# -------- PRODUCT --------
def create_product(db, data):
    obj = models.Product(**data.dict())
    db.add(obj)
    db.commit()
    return obj

def add_product_material(db, product_id, data):
    pm = models.ProductMaterial(
        product_id=product_id,
        material_id=data.material_id,
        qty_required=data.qty_required
    )
    db.add(pm)
    db.commit()

# -------- WORKER --------
def create_worker(db, data):
    w = models.Worker(**data.dict())
    db.add(w)
    db.commit()
    return w
