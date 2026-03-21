# ARQUIVO PRINCIPAL: Responsável por criar a instância do Flask, definir a Secret Key (para sessões) e dar o "Play" no servidor.

from flask import Flask
from configuration import configure_all

app = Flask(__name__)

app.secret_key = 'senha'

configure_all(app)


#executando a aplicação Flask
app.run(debug=True)
