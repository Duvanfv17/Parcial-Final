from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database.connection import Base



class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    descripcion = Column(String, nullable=True)

   
    eventos = relationship(
        "EventoTuristico",
        back_populates="categoria",
        cascade="all, delete-orphan"
    )


class Hotel(Base):
    __tablename__ = "hoteles"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, unique=True, index=True, nullable=False)
    contrasena = Column(String, nullable=False)
    nombre_hotel = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
    calificacion = Column(Float, nullable=False)


class EventoTuristico(Base):
    __tablename__ = "eventos_turisticos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    descripcion = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
    ubicacion = Column(String, nullable=False)

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id", ondelete="CASCADE"),
        nullable=False
    )

    categoria = relationship("Categoria", back_populates="eventos")



class RecomendacionVuelo(Base):
    __tablename__ = "recomendacion_vuelos"

    id = Column(Integer, primary_key=True, index=True)
    origen = Column(String, index=True, nullable=False)
    destino = Column(String, index=True, nullable=False)
    fecha_salida = Column(DateTime, nullable=False)
    fecha_regreso = Column(DateTime, nullable=False)
    precio = Column(Float, nullable=False)
