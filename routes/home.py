from flask import Blueprint, render_template, session, redirect, url_for

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home_view():
    
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view')) 

    return render_template('home.html')
    
