# API de Usuários com FastAPI

API REST completa para gerenciamento de usuários com autenticação JWT.

## Tecnologias
- Python
- FastAPI
- SQLite
- SQLAlchemy
- JWT (autenticação)

## Funcionalidades
- Criar usuário
- Listar usuários
- Atualizar usuário
- Deletar usuário
- Login com autenticação JWT

## Como rodar o projeto

```bash
pip install -r app/requirements.txt
python -m uvicorn app.main:app --reload
