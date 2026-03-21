# tela meu perfil no site, onde o usuário pode ver e editar suas informações pessoais, como nome, email e senha.

from flask import Blueprint, render_template, session, redirect, url_for

usuario_route = Blueprint('usuario', __name__)  

@usuario_route.route('/perfil')
def perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))

    
    return render_template('usuario.html')