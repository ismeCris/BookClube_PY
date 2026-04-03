# ROTAS DE AUTENTICAÇÃO: Lógica de Login, Cadastro e Logout. 
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database.models.usuario import Usuario
from werkzeug.security import check_password_hash, generate_password_hash

auth_route = Blueprint('auth', __name__)

from flask import make_response

@auth_route.route('/login', methods=['GET'])
def login_view():
    if 'usuario_id' in session:
        return redirect(url_for('home.home_view'))

    response = make_response(render_template('login.html'))
    response.headers["Cache-Control"] = "no-store"
    return response

@auth_route.route('/login', methods=['POST'])
def login_usuario():
    dados = request.form

    usuario = Usuario.get_or_none(Usuario.email == dados.get('email'))

    if usuario and check_password_hash(usuario.senha, dados.get('senha')):
        session['usuario_id'] = usuario.id
        return redirect(url_for('home.home_view'))
    else:
        flash("Email ou senha inválidos", "error")
        return redirect(url_for('auth.login_view'))
    
    
@auth_route.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        dados = request.form

        # verifica se já existe
        usuario_existente = Usuario.get_or_none(Usuario.email == dados.get('email'))

        if usuario_existente:
            flash("Email já cadastrado", "error")
            return redirect(url_for('auth.cadastro'))

        # cria usuário
        usuario = Usuario.create(
            nome=dados.get('nome'),
            email=dados.get('email'),
            senha=generate_password_hash(dados.get('senha'))
        )

        flash("Conta criada com sucesso!", "success")
        return redirect(url_for('auth.login_view'))

    return render_template('cadastro.html')

@auth_route.route('/logout')
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for('auth.login_view'))