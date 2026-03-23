from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.user import UsuarioCreate
from app.crud.user import criar_usuario, autenticar_usuario
from app.core.security import criar_token

router = APIRouter()  # 👈 ESSENCIAL

# conexão com banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# cadastro
@router.post("/register")
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)

# login
@router.post("/login")
def login(email: str, senha: str, db: Session = Depends(get_db)):
    user = autenticar_usuario(db, email, senha)
    
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token({"sub": user.email})
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }