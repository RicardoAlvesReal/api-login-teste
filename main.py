from fastapi import FastAPI, Form, Request, Depends, APIRouter, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
import secrets
import bcrypt
from email_validator import validate_email, EmailNotValidError
from datetime import datetime, timedelta # Adicionado

from database import get_db, Usuario
from auth import create_access_token, get_current_user, Token # Importações do auth.py

app = FastAPI()
api_router = APIRouter(prefix="/api") # Roteador para a API

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key=secrets.token_hex(32))

# Função para hash da senha
def hash_senha(senha: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Função para verificar senha
def verificar_senha(senha: str, hash_armazenado: str) -> bool:
    return bcrypt.checkpw(senha.encode('utf-8'), hash_armazenado.encode('utf-8'))

# Função para verificar se usuário está logado
def verificar_login(request: Request):
    return request.session.get("usuario_logado")

@app.get("/", response_class=HTMLResponse)
def login_form(request: Request):
    # Se já estiver logado, redireciona para dashboard
    if verificar_login(request):
        return RedirectResponse("/dashboard", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request, "mensagem": ""})

@app.post("/login", response_class=HTMLResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # Busca usuário no banco
    usuario = db.query(Usuario).filter(Usuario.username == username).first()
    
    if usuario and verificar_senha(password, usuario.password):
        # Cria sessão
        request.session["usuario_logado"] = username
        return RedirectResponse("/dashboard", status_code=302)
    
    return templates.TemplateResponse("login.html", {"request": request, "mensagem": "Usuário ou senha inválidos!"})

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    usuario = verificar_login(request)
    if not usuario:
        return RedirectResponse("/", status_code=302)
    return templates.TemplateResponse("dashboard.html", {"request": request, "usuario": usuario})

@app.get("/logout")
def logout(request: Request):
    # Remove a sessão
    request.session.clear()
    return RedirectResponse("/", status_code=302)

@app.get("/cadastro", response_class=HTMLResponse)
def cadastro_form(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request, "mensagem": ""})

@app.post("/cadastro", response_class=HTMLResponse)
def cadastrar(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # Valida o formato do email
    try:
        validate_email(email)
    except EmailNotValidError:
        return templates.TemplateResponse("cadastro.html", {"request": request, "mensagem": "Formato de email inválido!"})

    # Verifica se usuário ou email já existem
    usuario_existente = db.query(Usuario).filter(Usuario.username == username).first()
    if usuario_existente:
        return templates.TemplateResponse("cadastro.html", {"request": request, "mensagem": "Nome de usuário já existe!"})
    
    email_existente = db.query(Usuario).filter(Usuario.email == email).first()
    if email_existente:
        return templates.TemplateResponse("cadastro.html", {"request": request, "mensagem": "Email já cadastrado!"})
    
    # Cria novo usuário com senha hasheada
    senha_hash = hash_senha(password)
    novo_usuario = Usuario(username=username, email=email, password=senha_hash)
    
    db.add(novo_usuario)
    db.commit()
    
    return templates.TemplateResponse("login.html", {"request": request, "mensagem": "Cadastro realizado com sucesso! Faça login."})

# --- ROTAS DE RECUPERAÇÃO DE SENHA ---

@app.get("/recuperar-senha", response_class=HTMLResponse)
def recuperar_senha_form(request: Request):
    return templates.TemplateResponse("recuperar_senha.html", {"request": request, "mensagem": ""})

@app.post("/recuperar-senha", response_class=HTMLResponse)
def solicitar_recuperacao(request: Request, email: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        # Gera token seguro e define expiração (ex: 1 hora)
        token = secrets.token_urlsafe(32)
        expires = datetime.utcnow() + timedelta(hours=1)
        
        usuario.reset_token = token
        usuario.reset_token_expires = expires
        db.commit()
        
        # Em uma aplicação real, você enviaria este link por email
        link_recuperacao = f"http://localhost:8000/redefinir-senha/{token}"
        print(f"--- LINK DE RECUPERAÇÃO (COPIE E COLE NO NAVEGADOR) ---\n{link_recuperacao}\n----------------------------------------------------")
        
        return templates.TemplateResponse("login.html", {"request": request, "mensagem": "Link de recuperação enviado (verifique o console)!"})

    # Por segurança, não informe se o email não foi encontrado
    return templates.TemplateResponse("login.html", {"request": request, "mensagem": "Se o email existir, um link será enviado."})

@app.get("/redefinir-senha/{token}", response_class=HTMLResponse)
def redefinir_senha_form(request: Request, token: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.reset_token == token).first()
    if not usuario or usuario.reset_token_expires < datetime.utcnow():
        return templates.TemplateResponse("login.html", {"request": request, "mensagem": "Token inválido ou expirado!"})
    
    return templates.TemplateResponse("redefinir_senha.html", {"request": request, "token": token, "mensagem": ""})

@app.post("/redefinir-senha", response_class=HTMLResponse)
def redefinir_senha(request: Request, token: str = Form(...), nova_senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.reset_token == token).first()
    if not usuario or usuario.reset_token_expires < datetime.utcnow():
        return templates.TemplateResponse("login.html", {"request": request, "mensagem": "Token inválido ou expirado!"})

    usuario.password = hash_senha(nova_senha)
    usuario.reset_token = None
    usuario.reset_token_expires = None
    db.commit()

    return templates.TemplateResponse("login.html", {"request": request, "mensagem": "Senha redefinida com sucesso! Faça o login."})


# --- ENDPOINTS DA API REST ---

@api_router.post("/register", status_code=201)
def register_user_api(username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # Reutiliza a lógica de verificação e hash
    if db.query(Usuario).filter(Usuario.username == username).first():
        raise HTTPException(status_code=400, detail="Nome de usuário já existe")
    if db.query(Usuario).filter(Usuario.email == email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    hashed_password = hash_senha(password)
    new_user = Usuario(username=username, email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "Usuário criado com sucesso"}

@api_router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.username == form_data.username).first()
    if not user or not verificar_senha(form_data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@api_router.get("/users/me")
def read_users_me(current_user: Usuario = Depends(get_current_user)):
    # Retorna os dados do usuário logado (sem a senha)
    return {"username": current_user.username, "email": current_user.email}


# Inclui o roteador da API na aplicação principal
app.include_router(api_router)


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")