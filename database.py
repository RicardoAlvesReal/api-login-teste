from sqlalchemy import create_engine, Column, Integer, String, DateTime # Adicionado DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import re

# Configuração do banco SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./usuarios.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função de validação de email usando regex
def validar_email(email: str) -> bool:
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(padrao, email) is not None

# Modelo de usuário
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    reset_token = Column(String, unique=True, nullable=True) # Adicionado
    reset_token_expires = Column(DateTime, nullable=True)    # Adicionado

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()