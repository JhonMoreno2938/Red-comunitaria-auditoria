from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Credenciales de tu base de datos en Dokploy
DATABASE_URL = (
    "postgresql://postgres:postgres@192.168.0.107:5433/red_comunitaria"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependencia para obtener la sesión en los endpoints
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()