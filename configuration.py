from routes.home import home_route
from routes.usuario import usuario_route # Importe a nova rota
from database.database import db
from database.models.usuario import Usuario

def configure_all(app):
    configure_db()
    configure_routes(app)

def configure_routes(app):
    app.register_blueprint(home_route)
    # Adicionamos o prefixo /auth ou /usuario
    app.register_blueprint(usuario_route, url_prefix='/auth')

def configure_db():
    db.connect()
    # Adicione o modelo Usuario aqui para ele criar a tabela no MySQL
    db.create_tables([Usuario])