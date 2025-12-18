from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .database import get_db
from . import schemas, crud

router = APIRouter()

# =====================================================
# CLIENT ROUTES
# =====================================================

@router.post(
    "/clients",
    response_model=schemas.ClientOut,
    status_code=status.HTTP_201_CREATED
)
def create_client(
    data: schemas.ClientCreate,
    db: Session = Depends(get_db)
):
    return crud.create_client(db, data.dict())


@router.get(
    "/clients",
    response_model=List[schemas.ClientOut]
)
def list_clients(db: Session = Depends(get_db)):
    return crud.get_clients(db)


@router.get(
    "/clients/{client_id}",
    response_model=schemas.ClientOut
)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client topilmadi")
    return client


@router.put(
    "/clients/{client_id}",
    response_model=schemas.ClientOut
)
def update_client(
    client_id: int,
    data: schemas.ClientUpdate,
    db: Session = Depends(get_db)
):
    client = crud.update_client(db, client_id, data.dict())
    if not client:
        raise HTTPException(status_code=404, detail="Client topilmadi")
    return client


@router.delete(
    "/clients/{client_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_client(db, client_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Client topilmadi")
    return None


# =====================================================
# MATERIAL ROUTES
# =====================================================

@router.post(
    "/materials",
    response_model=schemas.MaterialOut,
    status_code=status.HTTP_201_CREATED
)
def create_material(
    data: schemas.MaterialCreate,
    db: Session = Depends(get_db)
):
    return crud.create_material(db, data.dict())


@router.get(
    "/materials",
    response_model=List[schemas.MaterialOut]
)
def list_materials(db: Session = Depends(get_db)):
    return crud.get_materials(db)


@router.get(
    "/materials/{material_id}",
    response_model=schemas.MaterialOut
)
def get_material(material_id: int, db: Session = Depends(get_db)):
    material = crud.get_material(db, material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material topilmadi")
    return material


@router.put(
    "/materials/{material_id}",
    response_model=schemas.MaterialOut
)
def update_material(
    material_id: int,
    data: schemas.MaterialUpdate,
    db: Session = Depends(get_db)
):
    material = crud.update_material(db, material_id, data.dict())
    if not material:
        raise HTTPException(status_code=404, detail="Material topilmadi")
    return material


@router.delete(
    "/materials/{material_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_material(material_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_material(db, material_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Material topilmadi")
    return None


# =====================================================
# MATERIAL STOCK + LOGS
# =====================================================

@router.post(
    "/materials/{material_id}/stock",
    response_model=schemas.MaterialStockOut
)
def update_material_stock(
    material_id: int,
    change: schemas.MaterialLogOut,
    db: Session = Depends(get_db)
):
    stock = crud.update_material_stock(
        db=db,
        material_id=material_id,
        change_qty=change.change_qty,
        reason=change.reason
    )
    if not stock:
        raise HTTPException(status_code=404, detail="Material stock topilmadi")
    return stock


@router.get(
    "/materials/low-stock",
    response_model=List[schemas.MaterialOut]
)
def get_low_stock_materials(db: Session = Depends(get_db)):
    return crud.get_low_stock_materials(db)


# =====================================================
# WORKER ROUTES
# =====================================================

@router.post(
    "/workers",
    response_model=schemas.WorkerOut,
    status_code=status.HTTP_201_CREATED
)
def create_worker(
    data: schemas.WorkerCreate,
    db: Session = Depends(get_db)
):
    return crud.create_worker(db, data.dict())


@router.get(
    "/workers",
    response_model=List[schemas.WorkerOut]
)
def list_workers(db: Session = Depends(get_db)):
    return crud.get_workers(db)


@router.get(
    "/workers/{worker_id}",
    response_model=schemas.WorkerOut
)
def get_worker(worker_id: int, db: Session = Depends(get_db)):
    worker = crud.get_worker(db, worker_id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker topilmadi")
    return worker


@router.put(
    "/workers/{worker_id}",
    response_model=schemas.WorkerOut
)
def update_worker(
    worker_id: int,
    data: schemas.WorkerUpdate,
    db: Session = Depends(get_db)
):
    worker = crud.update_worker(db, worker_id, data.dict())
    if not worker:
        raise HTTPException(status_code=404, detail="Worker topilmadi")
    return worker


@router.delete(
    "/workers/{worker_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_worker(db, worker_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Worker topilmadi")
    return None


# =====================================================
# PRODUCT ROUTES
# =====================================================

@router.post(
    "/products",
    response_model=schemas.ProductOut,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    data: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, data.dict())


@router.get(
    "/products",
    response_model=List[schemas.ProductOut]
)
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@router.get(
    "/products/{product_id}",
    response_model=schemas.ProductOut
)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product topilmadi")
    return product


@router.put(
    "/products/{product_id}",
    response_model=schemas.ProductOut
)
def update_product(
    product_id: int,
    data: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):
    product = crud.update_product(db, product_id, data.dict())
    if not product:
        raise HTTPException(status_code=404, detail="Product topilmadi")
    return product


@router.delete(
    "/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_product(db, product_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Product topilmadi")
    return None


# =====================================================
# PRODUCT MATERIALS
# =====================================================

@router.post(
    "/products/{product_id}/materials",
    response_model=schemas.ProductMaterialOut,
    status_code=status.HTTP_201_CREATED
)
def add_material_to_product(
    product_id: int,
    data: schemas.ProductMaterialCreate,
    db: Session = Depends(get_db)
):
    return crud.add_material_to_product(
        db=db,
        product_id=product_id,
        material_id=data.material_id,
        qty_required=data.qty_required
    )


@router.get(
    "/products/{product_id}/materials",
    response_model=List[schemas.ProductMaterialOut]
)
def get_product_materials(
    product_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_product_materials(db, product_id)


# =====================================================
# WORK LOGS + REPORTS
# =====================================================

@router.post(
    "/work-logs",
    response_model=schemas.WorkLogOut,
    status_code=status.HTTP_201_CREATED
)
def add_work_log(
    data: schemas.WorkLogCreate,
    db: Session = Depends(get_db)
):
    return crud.add_work_log(
        db=db,
        worker_id=data.worker_id,
        product_id=data.product_id,
        quantity=data.quantity,
        work_date=data.work_date
    )


@router.get(
    "/reports/worker-production",
    response_model=List[schemas.WorkerProductionOut]
)
def worker_production_report(db: Session = Depends(get_db)):
    return crud.get_worker_production(db)
