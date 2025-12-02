from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas
from app.database.connection import get_db

router = APIRouter(prefix="/vuelos", tags=["Recomendación de Vuelos"])

@router.post("/", response_model=schemas.RecomendacionVueloOut)
def crear(data: schemas.RecomendacionVueloCreate, db: Session = Depends(get_db)):
    vuelo = models.RecomendacionVuelo(**data.dict())
    db.add(vuelo)
    db.commit()
    db.refresh(vuelo)
    return vuelo

@router.get("/", response_model=list[schemas.RecomendacionVueloOut])
def listar(db: Session = Depends(get_db)):
    return db.query(models.RecomendacionVuelo).all()

@router.get("/{id}", response_model=schemas.RecomendacionVueloOut)
def obtener(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.RecomendacionVuelo).filter(models.RecomendacionVuelo.id == id).first()
    if not obj:
        raise HTTPException(404, "Vuelo no encontrado")
    return obj

@router.put("/{id}", response_model=schemas.RecomendacionVueloOut)
def actualizar(id: int, data: schemas.RecomendacionVueloCreate, db: Session = Depends(get_db)):
    obj = db.query(models.RecomendacionVuelo).filter(models.RecomendacionVuelo.id == id).first()
    if not obj:
        raise HTTPException(404, "Vuelo no encontrado")

    for k, v in data.dict().items():
        setattr(obj, k, v)

    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.RecomendacionVuelo).filter(models.RecomendacionVuelo.id == id).first()
    if not obj:
        raise HTTPException(404, "Vuelo no encontrado")

    db.delete(obj)
    db.commit()
    return {"mensaje": "Vuelo eliminado"}
