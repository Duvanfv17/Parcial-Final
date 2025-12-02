from fastapi import FastAPI
from app.api.routers import categorias, recomendacionvuelos, asignacionhoteles, eventosturisticos
from app.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AventaTravel Group API",
    description="API para gestión turística: categorías, hoteles, vuelos y eventos",
    version="1.0.0"
)


app.include_router(categorias.router)
app.include_router(recomendacionvuelos.router)
app.include_router(asignacionhoteles.router)
app.include_router(eventosturisticos.router)


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a AventaTravel Group"}
