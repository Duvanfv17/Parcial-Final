from pydantic import BaseModel
from datetime import datetime


class CategoriaBase(BaseModel):
    nombre: str
    descripcion: str    

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaOut(CategoriaBase):
    id: int
    class Config:
        from_attributes = True



class HotelBase(BaseModel):
    usuario: str
    contrasena: str
    nombre_hotel: str
    ubicacion: str
    calificacion: float

class HotelCreate(HotelBase):
    pass    

class HotelOut(HotelBase):
    id: int
    class Config:
        from_attributes = True



class EventoBase(BaseModel):
    nombre: str
    descripcion: str
    fecha: datetime
    ubicacion: str
    categoria_id: int
    
class EventoCreate(EventoBase):
    pass    

class EventoOut(EventoBase):
    id: int
    class Config:
        from_attributes = True



class RecomendacionVueloBase(BaseModel):
    origen: str
    destino: str
    fecha_salida: datetime
    fecha_regreso: datetime
    precio: float

class RecomendacionVueloCreate(RecomendacionVueloBase):
    pass    

class RecomendacionVueloOut(RecomendacionVueloBase):
    id: int
    class Config:
        from_attributes = True
