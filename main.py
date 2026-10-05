from datetime import datetime
from database import engine, get_db
from fastapi import Depends, FastAPI, Query
from models import Base, ConexionCreate, ConexionDB
from sqlalchemy.orm import Session

# Crear las tablas automáticamente si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Red Comunitaria",
    description="API modular para el registro y consulta de dispositivos",
    version="1.0.0",
)


@app.get("/")
def home():
  return {"mensaje": "Bienvenido a la API de la Red Comunitaria"}


# Endpoint POST para registrar una nueva conexión
@app.post("/api/conexiones", status_code=201)
def registrar_conexion(conexion: ConexionCreate, db: Session = Depends(get_db)):
  nuevo_registro = ConexionDB(
      ip_asignada=conexion.ip_asignada,
      nombre_dispositivo=conexion.nombre_dispositivo,
      mac_address=conexion.mac_address,
  )
  db.add(nuevo_registro)
  db.commit()
  db.refresh(nuevo_registro)
  return {
      "mensaje": "Conexión registrada con éxito",
      "id": nuevo_registro.id,
      "datos": nuevo_registro,
  }


# Endpoint GET para consultar y filtrar por rango de fecha y hora
@app.get("/api/conexiones")
def obtener_conexiones(
    fecha_inicio: datetime | None = Query(
        None, description="Ej: 2026-10-01T00:00:00"
    ),
    fecha_fin: datetime | None = Query(
        None, description="Ej: 2026-10-05T23:59:59"
    ),
    db: Session = Depends(get_db),
):
  query = db.query(ConexionDB)

  if fecha_inicio:
    query = query.filter(ConexionDB.fecha_hora >= fecha_inicio)
  if fecha_fin:
    query = query.filter(ConexionDB.fecha_hora <= fecha_fin)

  resultados = query.order_by(ConexionDB.fecha_hora.desc()).all()
  return resultados