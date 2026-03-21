# tela meu perfil no site, onde o usuário pode ver e editar suas informações pessoais, como nome, email e senha.
from flask import Blueprint, render_template, request, session, redirect, url_for
from database.models.usuario import Usuario

usuario_route = Blueprint('usuario', __name__)  

@usuario_route.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))

    usuario = Usuario.get_or_none(Usuario.id == session['usuario_id'])

    if not usuario:
        return redirect(url_for('auth.login_view'))

    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
        usuario.telefone = request.form.get('telefone')
        usuario.endereco = request.form.get('endereco')

        usuario.save()

        return redirect(url_for('usuario.perfil'))

    return render_template('usuario.html', usuario=usuario)

@usuario_route.route('/editar-perfil', methods=['GET', 'POST'])
def editar_perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))

    usuario = Usuario.get_or_none(Usuario.id == session['usuario_id'])

    if not usuario:
        return redirect(url_for('auth.login_view'))

    return render_template('usuario.html', usuario=usuario)