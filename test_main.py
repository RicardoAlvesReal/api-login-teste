from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from main import app
from database import Base, get_db

# --- Configuração do Banco de Dados de Teste ---
# Usaremos um banco de dados SQLite em memória para os testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria as tabelas no banco de teste
Base.metadata.create_all(bind=engine)

# --- Sobrescreve a dependência get_db para usar o banco de teste ---
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Cria um cliente de teste para fazer requisições à API
client = TestClient(app)

# --- Testes ---

def test_register_user_api_success():
    """ Testa o registro de um novo usuário com sucesso. """
    response = client.post(
        "/api/register",
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword"
        }
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Usuário criado com sucesso"}

def test_register_user_api_duplicate_username():
    """ Testa a falha ao registrar um usuário com username duplicado. """
    # Primeiro, cria um usuário para garantir que ele exista
    client.post("/api/register", data={"username": "duplicate", "email": "duplicate@example.com", "password": "password"})
    
    # Tenta criar o mesmo usuário novamente
    response = client.post(
        "/api/register",
        data={
            "username": "duplicate",
            "email": "another@example.com",
            "password": "anotherpassword"
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Nome de usuário já existe"}

def test_login_for_access_token():
    """ Testa o login e a obtenção de um token de acesso. """
    # Cria um usuário para o teste de login
    client.post("/api/register", data={"username": "loginuser", "email": "login@example.com", "password": "loginpassword"})

    response = client.post(
        "/api/token",
        data={"username": "loginuser", "password": "loginpassword"}
    )
    assert response.status_code == 200
    json_data = response.json()
    assert "access_token" in json_data
    assert json_data["token_type"] == "bearer"