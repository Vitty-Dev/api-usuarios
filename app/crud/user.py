from sqlalchemy.orm import Session
from app.models.user import Usuario
from app.schemas.user import UsuarioCreate
from app.core.security import hash_senha, verificar_senha

def criar_usuario(db: Session, usuario: UsuarioCreate):
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=hash_senha(usuario.senha)
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def autenticar_usuario(db: Session, email: str, senha: str):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()

    if not usuario:
        return None

    if not verificar_senha(senha, usuario.senha):
        return None

    return usuario