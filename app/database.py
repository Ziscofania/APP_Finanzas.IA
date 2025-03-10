from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL de conexión de Neon.tech (cámbiala con tus credenciales)
DATABASE_URL = "postgresql://neondb_owner:npg_glId7Fa3yRmo@ep-frosty-mountain-a8xwvqio-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"

# Configuración del motor SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modelo Base
Base = declarative_base()

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
