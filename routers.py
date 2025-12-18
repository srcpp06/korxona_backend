from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter()

# CLIENT
@router.post("/clients")
def add_client(data: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, data)

@router.put("/clients/{id}")
def upd_client(id: int, data: schemas.ClientUpdate, db: Session = Depends(get_db)):
    return crud.update_client(db, id, data)

# MATERIAL
@router.post("/materials")
def add_material(data: schemas.MaterialCreate, db: Session = Depends(get_db)):
    return crud.create_material(db, data)

@router.post("/materials/in")
def material_in(data: schemas.MaterialInOut, db: Session = Depends(get_db)):
    crud.material_in(db, data.material_id, data.quantity, "kirim")
    return {"status":"ok"}

@router.post("/materials/out")
def material_out(data: schemas.MaterialInOut, db: Session = Depends(get_db)):
    crud.material_in(db, data.material_id, -data.quantity, "chiqim")
    return {"status":"ok"}

# PRODUCT
@router.post("/products")
def add_product(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, data)

@router.post("/products/{id}/materials")
def add_pm(id: int, data: schemas.ProductMaterialCreate, db: Session = Depends(get_db)):
    crud.add_product_material(db, id, data)
    return {"status":"linked"}

# WORKER
@router.post("/workers")
def add_worker(data: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.create_worker(db, data)
