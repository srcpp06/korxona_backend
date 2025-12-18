from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter()

@router.post("/clients", response_model=schemas.ClientOut)
def create_client(data: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, data)


@router.post("/materials/in")
def material_in(data: schemas.MaterialInOut, db: Session = Depends(get_db)):
    crud.material_kirim(db, data.material_id, data.quantity)
    return {"status": "ok"}
