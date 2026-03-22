# ARQUIVO PRINCIPAL: Responsável por criar a instância do Flask, definir a Secret Key (para sessões) e dar o "Play" no servidor.

from flask import Flask
from configuration import configure_all
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

configure_all(app)


#executando a aplicação Flask
app.run(debug=True)
