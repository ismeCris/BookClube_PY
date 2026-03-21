from flask import Blueprint, render_template, session, redirect, url_for

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home_view():
    # Se o usuário não tiver o "carimbo" (ID) na sessão, ele é mandado para a tela de login.
    if 'usuario_id' not in session:
        return redirect(url_for('home.login_view'))
    # Se estiver logado, carrega a tela principal (home.html)
    return render_template('home.html')
