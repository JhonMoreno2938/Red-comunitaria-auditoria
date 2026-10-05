from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String
from database import Base


# Modelo SQLAlchemy (La tabla en la base de datos)
class ConexionDB(Base):
  __tablename__ = "conexiones_dispositivos"

  id = Column(Integer, primary_key=True, index=True)
  fecha_hora = Column(DateTime, default=datetime.utcnow)
  ip_asignada = Column(String(45), nullable=False)
  nombre_dispositivo = Column(String(255))
  mac_address = Column(String(50))


# Esquema Pydantic (Validación de datos de entrada vía API)
class ConexionCreate(BaseModel):
  ip_asignada: str
  nombre_dispositivo: str | None = None
  mac_address: str | None = None