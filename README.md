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

### 2. Instale as dependências
```bash
pip install fastapi uvicorn jinja2 python-multipart itsdangerous sqlalchemy bcrypt pytest
```

### 3. Execute a aplicação
```bash
uvicorn main:app --reload
```

### 4. Acesse no navegador
- **Aplicação:** http://localhost:8000
- **Documentação API:** http://localhost:8000/docs

## 📖 Como Usar

### 1. **Cadastro de Usuário**
- Acesse `/cadastro` ou clique em "Cadastrar novo usuário"
- Insira nome de usuário, senha e email
- Clique em "Cadastrar"

### 2. **Login**
- Na página inicial, insira suas credenciais
- Clique em "Entrar"
- Será redirecionado para o dashboard

### 3. **Dashboard**
- Área protegida que só usuários logados podem acessar
- Exibe informações do usuário logado
- Botão de logout disponível

### 4. **Logout**
- Clique em "Logout Seguro" no dashboard
- Sessão será limpa e redirecionamento para login

### 5. **Recuperação de Senha**
- Acesse `/recuperar_senha`
- Insira seu email
- Siga as instruções enviadas por email

### 6. **Redefinição de Senha**
- Acesse `/redefinir_senha`
- Insira sua nova senha
- Confirme a nova senha
- Clique em "Redefinir Senha"

## 🛡️ Segurança

- **Sessões criptografadas** com chave secreta aleatória
- **Middleware de sessão** do Starlette
- **Proteção de rotas** - dashboard só acessível se logado
- **Redirecionamentos automáticos** para páginas apropriadas
- **Tokens seguros** para recuperação de senha
- **Hash de senhas** com bcrypt

## 🔄 Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Página de login |
| POST | `/login` | Processa login |
| GET | `/cadastro` | Página de cadastro |
| POST | `/cadastro` | Processa cadastro |
| GET | `/dashboard` | Dashboard protegido |
| GET | `/logout` | Logout e limpeza de sessão |
| GET | `/recuperar_senha` | Página de recuperação de senha |
| POST | `/recuperar_senha` | Envia email de recuperação |
| GET | `/redefinir_senha` | Página de redefinição de senha |
| POST | `/redefinir_senha` | Atualiza senha no banco de dados |
| GET | `/favicon.ico` | Ícone do site |

## ⚠️ Observações

- **Para desenvolvimento apenas**: Os usuários são armazenados em memória
- **Senhas em texto puro**: Para produção, use hash (bcrypt, argon2, etc.)
- **Banco de dados**: Para produção, implemente SQLite, PostgreSQL, etc.

## 🚀 Melhorias Futuras

- [ ] Validação de email
- [ ] CSS/Bootstrap para interface
- [ ] API REST endpoints
- [ ] Testes automatizados

## 📝 Licença

Este projeto é livre para uso educacional e desenvolvimento.

---

**Desenvolvido com ❤️ usando FastAPI**

