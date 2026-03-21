# CONFIGURAÇÕES: Centraliza o registro de Blueprints (rotas) e a inicialização das tabelas do Banco de Dados (MySQL).
from flask import session, redirect, url_for, request
from routes.home import home_route       
from routes.Login import auth_route      
from database.database import db
from database.models.usuario import Usuario

def configurar_seguranca(app):
    @app.before_request
    def verificar_acesso():
        # Verifique se no Login.py o blueprint chama-se 'auth'
        rotas_publicas = ['auth.login_view', 'auth.login_usuario', 'static']
        # Ignora a verificação se for uma rota que não existe (evita erro 500)
        if request.endpoint is None:
            return

        if request.endpoint not in rotas_publicas and 'usuario_id' not in session:
          return redirect(url_for('auth.login_view'))

def configure_all(app):
    configure_db()
    configure_routes(app)
    configurar_seguranca(app)

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(auth_route, url_prefix='/auth')


def configure_db():
    db.connect()
    db.create_tables([Usuario])