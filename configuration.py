from flask import session, redirect, url_for, request

from routes.home import home_route       
from routes.login import auth_route  
from routes.usuario import usuario_route    
from routes.livro import livro_route
from routes.clube import clube_route

from database.database import db
from database.models.usuario import Usuario
from database.models.clube import Clube
from database.models.usuario_clube import UsuarioClube  
from database.models.livro import Livro  

def configurar_seguranca(app):
    @app.before_request
    def verificar_acesso():
        rotas_publicas = ['auth.login_view', 'auth.login_usuario', 'auth.cadastro', 'static']

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
    app.register_blueprint(usuario_route, url_prefix='/usuario')
    app.register_blueprint(livro_route, url_prefix='/livros')
    app.register_blueprint(clube_route, url_prefix='/clubes')

def configure_db():
    db.connect()

    #db.drop_tables([UsuarioClube, Clube, Usuario, Livro]) 
    db.create_tables([Usuario, Clube, Livro, UsuarioClube])
