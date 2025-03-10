from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User

router = APIRouter()

# Obtener todos los usuarios
@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# Crear un usuario
@router.post("/users")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
