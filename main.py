from flask import Flask
from configuration import configure_all

app = Flask(__name__)

configure_all(app)


#executando a aplicação Flask
app.run(debug=True)
