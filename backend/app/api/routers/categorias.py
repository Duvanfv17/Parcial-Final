from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import models
from app.schemas import schemas
from app.database.connection import SessionLocal

router = APIRouter(prefix="/categorias", tags=["Categorias"])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.CategoriaOut)
def crear_categoria(data: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    categoria = models.Categoria(**data.model_dump())
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria


@router.get("/", response_model=list[schemas.CategoriaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(models.Categoria).all()


@router.get("/{id}", response_model=schemas.CategoriaOut)
def obtener(id: int, db: Session = Depends(get_db)):
    item = db.query(models.Categoria).filter(models.Categoria.id == id).first()
    if not item:
        raise HTTPException(404, "Categoría no encontrada")
    return item


@router.put("/{id}", response_model=schemas.CategoriaOut)
def actualizar(id: int, data: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    item = db.query(models.Categoria).filter(models.Categoria.id == id).first()
    if not item:
        raise HTTPException(404, "Categoría no encontrada")

    for key, value in data.model_dump().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    item = db.query(models.Categoria).filter(models.Categoria.id == id).first()
    if not item:
        raise HTTPException(404, "Categoría no encontrada")

    db.delete(item)
    db.commit()
    return {"mensaje": "Categoría eliminada correctamente"}

