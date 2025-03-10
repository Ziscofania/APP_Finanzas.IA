from fastapi import FastAPI
from app.routes import user
from app.database import engine, Base

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "¡API funcionando correctamente!"}
