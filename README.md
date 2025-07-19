# API de Login com FastAPI

Uma aplicação web simples de autenticação desenvolvida com FastAPI, incluindo sistema de login, cadastro de usuários e dashboard protegido.

## 🚀 Funcionalidades

- ✅ **Login de usuários** com validação
- ✅ **Cadastro de novos usuários** com validação de email
- ✅ **Dashboard protegido** com sessões
- ✅ **Logout seguro** com limpeza de sessão
- ✅ **Recuperação de senha** com token seguro
- ✅ **Interface web** responsiva com Bootstrap
- ✅ **API REST** com autenticação JWT
- ✅ **Senhas seguras** com hash bcrypt
- ✅ **Banco de dados SQLite** para persistência de dados
- ✅ **Testes automatizados** com Pytest

## 🛠️ Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido para Python
- **SQLAlchemy** - ORM para interação com o banco de dados
- **Jinja2** - Engine de templates para renderização HTML
- **Bootstrap** - Framework CSS para interface responsiva
- **Bcrypt** - Biblioteca para hash de senhas
- **Pytest** - Framework para testes automatizados
- **Python 3.10+** - Linguagem de programação

## 📁 Estrutura do Projeto

```
api-login-teste/
├── main.py                 # Aplicação principal FastAPI
├── auth.py                 # Lógica de autenticação JWT
├── database.py             # Configuração do banco de dados
├── test_main.py            # Testes automatizados
├── usuarios.db             # Arquivo do banco de dados SQLite
├── templates/              # Templates HTML
│   ├── base.html
│   ├── login.html
│   ├── cadastro.html
│   ├── dashboard.html
│   ├── recuperar_senha.html
│   └── redefinir_senha.html
├── static/                 # Arquivos estáticos
│   ├── favicon.ico
│   └── TJES-logo.png
└── README.md               # Este arquivo
```

## 🔧 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd api-login-teste
```

### 2. Crie e ative um ambiente virtual (Recomendado)
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
Anotei para não esquecer do comando para criar o "TXT".
*(Nota: Você precisará criar um arquivo `requirements.txt` com `pip freeze > requirements.txt`)*

### 4. Execute a aplicação
```bash
uvicorn main:app --reload
```

### 5. Acesse no navegador
- **Aplicação Web:** http://localhost:8000
- **Documentação da API:** http://localhost:8000/docs

## 📖 Como Usar

A aplicação possui uma interface web intuitiva para cadastro, login, recuperação de senha e um dashboard. A API REST pode ser utilizada por outras aplicações para autenticação.

## 🛡️ Segurança

- **Senhas com Hash**: As senhas são protegidas usando `bcrypt`.
- **Sessões Criptografadas**: A interface web usa sessões seguras do Starlette.
- **Tokens JWT**: A API REST é protegida com JSON Web Tokens.
- **Proteção de Rotas**: Rotas sensíveis (como o dashboard) são protegidas.

## 🔄 Rotas da API

| Método | Rota | Descrição | Autenticação |
|--------|------|-----------|--------------|
| POST | `/api/register` | Registra um novo usuário | Nenhuma |
| POST | `/api/token` | Realiza login e retorna um token JWT | Nenhuma |
| GET | `/api/users/me`| Retorna dados do usuário logado | Token JWT |

## 🚀 Melhorias Futuras

- [x] Hash de senhas com bcrypt
- [x] Banco de dados SQLite/PostgreSQL
- [x] Validação de email
- [x] Recuperação de senha
- [x] CSS/Bootstrap para interface
- [x] API REST endpoints
- [x] Testes automatizados

## 📝 Licença

Este projeto é livre para uso educacional e desenvolvimento.

---

**Desenvolvido com ❤️ usando FastAPI**