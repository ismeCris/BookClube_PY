# ARQUIVO PRINCIPAL: Responsável por criar a instância do Flask, definir a Secret Key (para sessões) e dar o "Play" no servidor.

from flask import Flask, redirect, request, session, url_for
from configuration import configure_all
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.before_request
def proteger_rotas():
    rotas_livres = [
        'auth.login_view',
        'auth.login_usuario',
        'auth.cadastro',
        'static'
    ]

    if request.endpoint not in rotas_livres:
        if 'usuario_id' not in session:
            return redirect(url_for('auth.login_view'))

app.secret_key = os.getenv('SECRET_KEY')

configure_all(app)


    
#executando a aplicação Flask
app.run(debug=True)
