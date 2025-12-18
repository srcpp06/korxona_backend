from sqlalchemy.orm import Session
import models

def create_client(db: Session, data):
    client = models.Client(**data.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


def material_kirim(db: Session, material_id, qty):
    stock = db.query(models.MaterialStock).get(material_id)
    if not stock:
        stock = models.MaterialStock(material_id=material_id, quantity=0)
        db.add(stock)

    stock.quantity += qty

    log = models.MaterialLog(
        material_id=material_id,
        change_qty=qty,
        reason="kirim"
    )

    db.add(log)
    db.commit()
