# API de Login com FastAPI

Uma aplicação web simples de autenticação desenvolvida com FastAPI, incluindo sistema de login, cadastro de usuários e dashboard protegido.

## 🚀 Funcionalidades

- ✅ **Login de usuários** com validação
- ✅ **Cadastro de novos usuários**
- ✅ **Dashboard protegido** com sessões
- ✅ **Logout seguro** com limpeza de sessão
- ✅ **Interface web** responsiva com templates HTML
- ✅ **Favicon e logo personalizados**
- ✅ **Middleware de sessão** para segurança

## 🛠️ Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido para Python
- **Jinja2** - Engine de templates para renderização HTML
- **Starlette** - Framework ASGI para middleware de sessões
- **Python 3.10+** - Linguagem de programação

## 📁 Estrutura do Projeto

```
api-login-teste/
├── main.py                 # Aplicação principal FastAPI
├── templates/              # Templates HTML
│   ├── login.html          # Página de login
│   ├── cadastro.html       # Página de cadastro
│   └── dashboard.html      # Dashboard do usuário
├── static/                 # Arquivos estáticos
│   ├── favicon.ico         # Ícone do site
│   └── TJES-logo.png      # Logo da aplicação
└── README.md              # Este arquivo
```

## 🔧 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd api-login-teste
```

### 2. Instale as dependências
```bash
pip install fastapi uvicorn jinja2 python-multipart itsdangerous
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
- Insira nome de usuário e senha
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

## 🛡️ Segurança

- **Sessões criptografadas** com chave secreta aleatória
- **Middleware de sessão** do Starlette
- **Proteção de rotas** - dashboard só acessível se logado
- **Redirecionamentos automáticos** para páginas apropriadas

## 🔄 Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Página de login |
| POST | `/login` | Processa login |
| GET | `/cadastro` | Página de cadastro |
| POST | `/cadastro` | Processa cadastro |
| GET | `/dashboard` | Dashboard protegido |
| GET | `/logout` | Logout e limpeza de sessão |
| GET | `/favicon.ico` | Ícone do site |

## ⚠️ Observações

- **Para desenvolvimento apenas**: Os usuários são armazenados em memória
- **Senhas em texto puro**: Para produção, use hash (bcrypt, argon2, etc.)
- **Banco de dados**: Para produção, implemente SQLite, PostgreSQL, etc.

## 🚀 Melhorias Futuras

- [ ] Hash de senhas com bcrypt
- [ ] Banco de dados SQLite/PostgreSQL
- [ ] Validação de email
- [ ] Recuperação de senha
- [ ] CSS/Bootstrap para interface
- [ ] API REST endpoints
- [ ] Testes automatizados

## 📝 Licença

Este projeto é livre para uso educacional e desenvolvimento.

---

**Desenvolvido com ❤️ usando FastAPI**

