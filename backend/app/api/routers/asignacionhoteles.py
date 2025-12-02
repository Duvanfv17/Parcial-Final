from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas
from app.database.connection import get_db

router = APIRouter(prefix="/hoteles", tags=["Asignación Hoteles"])



@router.post("/", response_model=schemas.HotelOut)
def crear(data: schemas.HotelCreate, db: Session = Depends(get_db)):
    hotel = models.AsignacionHotel(**data.model_dump())
    db.add(hotel)
    db.commit()
    db.refresh(hotel)
    return hotel



@router.get("/", response_model=list[schemas.HotelOut])
def listar(db: Session = Depends(get_db)):
    return db.query(models.AsignacionHotel).all()



@router.get("/{id}", response_model=schemas.HotelOut)
def obtener(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.AsignacionHotel).filter(models.AsignacionHotel.id == id).first()
    if not obj:
        raise HTTPException(404, "Hotel no encontrado")
    return obj



@router.put("/{id}", response_model=schemas.HotelOut)
def actualizar(id: int, data: schemas.HotelCreate, db: Session = Depends(get_db)):
    obj = db.query(models.AsignacionHotel).filter(models.AsignacionHotel.id == id).first()
    if not obj:
        raise HTTPException(404, "Hotel no encontrado")

    for k, v in data.model_dump().items():
        setattr(obj, k, v)

    db.commit()
    db.refresh(obj)
    return obj



@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.AsignacionHotel).filter(models.AsignacionHotel.id == id).first()
    if not obj:
        raise HTTPException(404, "Hotel no encontrado")

    db.delete(obj)
    db.commit()
    return {"mensaje": "Hotel eliminado"}
