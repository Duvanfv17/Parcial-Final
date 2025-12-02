from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas
from app.database.connection import SessionLocal


router = APIRouter(prefix="/eventos", tags=["Eventos Turísticos"])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.EventoOut)
def crear(data: schemas.EventoCreate, db: Session = Depends(get_db)):
    ev = models.EventoTuristico(**data.dict())
    db.add(ev)
    db.commit()
    db.refresh(ev)
    return ev


@router.get("/", response_model=list[schemas.EventoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(models.EventoTuristico).all()


@router.get("/{id}", response_model=schemas.EventoOut)
def obtener(id: int, db: Session = Depends(get_db)):
    ev = db.query(models.EventoTuristico).filter(models.EventoTuristico.id == id).first()
    if not ev:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return ev


@router.put("/{id}", response_model=schemas.EventoOut)
def actualizar(id: int, data: schemas.EventoCreate, db: Session = Depends(get_db)):
    ev = db.query(models.EventoTuristico).filter(models.EventoTuristico.id == id).first()
    if not ev:
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    for k, v in data.dict().items():
        setattr(ev, k, v)

    db.commit()
    db.refresh(ev)
    return ev


@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    ev = db.query(models.EventoTuristico).filter(models.EventoTuristico.id == id).first()
    if not ev:
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    db.delete(ev)
    db.commit()
    return {"mensaje": "Evento eliminado"}
