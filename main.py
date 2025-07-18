from fastapi import FastAPI, Form, Request, Response, Cookie
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import secrets

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=secrets.token_hex(32))

templates = Jinja2Templates(directory="templates")

# Lista de usuários (em memória, para exemplo)
usuarios = []

app.mount("/static", StaticFiles(directory="static"), name="static")

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
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
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
def cadastrar(request: Request, username: str = Form(...), password: str = Form(...)):
    # Verifica se usuário já existe
    for usuario in usuarios:
        if usuario["username"] == username:
            return templates.TemplateResponse("cadastro.html", {"request": request, "mensagem": "Usuário já existe!"})
    usuarios.append({"username": username, "password": password})
    return templates.TemplateResponse("login.html", {"request": request, "mensagem": "Cadastro realizado com sucesso! Faça login."})

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")