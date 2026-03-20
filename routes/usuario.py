from flask import Blueprint, request, render_template, redirect, url_for
from database.models.usuario import Usuario 
from werkzeug.security import generate_password_hash, check_password_hash

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    # Pega os dados do formulário HTML
    dados = request.form
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')

    # Criptografa a senha antes de salvar
    senha_hash = generate_password_hash(senha)

    # Cria no banco
    Usuario.create(nome=nome, email=email, senha=senha_hash)
    
    return redirect(url_for('home.home_index')) # Redireciona após cadastrar

@usuario_route.route('/login', methods=['POST'])
def login_usuario():
    dados = request.form
    email = dados.get('email')
    senha = dados.get('senha')

    # Busca o usuário no banco
    usuario = Usuario.get_or_none(Usuario.email == email)

    if usuario and check_password_hash(usuario.senha, senha):
        return "Login realizado com sucesso!"
    else:
        return "E-mail ou senha incorretos!", 401