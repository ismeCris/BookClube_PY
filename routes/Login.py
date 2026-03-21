# ROTAS DE AUTENTICAÇÃO: Lógica de Login, Cadastro e Logout. 
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database.models.usuario import Usuario
from werkzeug.security import check_password_hash

auth_route = Blueprint('auth', __name__)

@auth_route.route('/login', methods=['GET'])
def login_view():
    return render_template('login.html')


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


@auth_route.route('/logout')
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for('auth.login_view'))