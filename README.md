# API de Usuários

API REST completa para gerenciamento de usuários, desenvolvida com foco em boas práticas de backend, autenticação segura e organização de código.

---

## Sobre o projeto

Esta API permite o cadastro, autenticação e gerenciamento de usuários, utilizando autenticação baseada em token (JWT).

O projeto foi desenvolvido com o objetivo de praticar conceitos importantes de desenvolvimento backend, como:

* Estruturação de APIs REST
* Autenticação e autorização
* Integração com banco de dados
* Organização em camadas (routers, schemas, models, etc.)

---

## Tecnologias utilizadas

* **Python**
* **FastAPI**
* **SQLite**
* **SQLAlchemy**
* **JWT (JSON Web Token)**
* **Uvicorn**

---

## Funcionalidades

* ✅ Cadastro de usuários
* ✅ Login com autenticação JWT
* ✅ Proteção de rotas autenticadas
* ✅ CRUD completo de usuários
* ✅ Validação de dados com Pydantic

---

## 📁 Estrutura do projeto

```
app/
├── routers/
│   ├── auth.py
│   └── users.py
├── auth.py
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
```

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Vitoria-Eduarda-Dev/api-usuarios.git
cd api-usuarios
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com:

```env
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 5. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

---

## Documentação automática

A API possui documentação interativa gerada automaticamente pelo FastAPI:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## Autenticação

A autenticação é feita utilizando **JWT (JSON Web Token)**.

Fluxo:

1. Usuário faz login
2. Recebe um token
3. Envia o token nas requisições protegidas

---

## Melhorias futuras

* 🔹 Deploy da aplicação
* 🔹 Integração com banco de dados PostgreSQL
* 🔹 Testes automatizados
* 🔹 Dockerização

---

## Autora

Desenvolvido por **Vitória Eduarda**
🔗 GitHub: https://github.com/Vitoria-Eduarda-Dev

---

## Licença

Este projeto está sob a licença MIT.
