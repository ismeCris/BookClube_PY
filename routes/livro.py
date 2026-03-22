from flask import Blueprint, render_template, request, redirect, url_for
from database.models.livro import Livro

livro_route = Blueprint('livro', __name__)

@livro_route.route('/')
def lista_livros():
    todos_os_livros= Livro.select()
    return render_template('livros.html', livros=todos_os_livros)

@livro_route.route('/salvar', methods=['POST'])
def salvar_livro():
    Livro.create(
        titulo=request.form.get('titulo'),
        autor=request.form.get('autor'),
        sinopse=request.form.get('descricao'), 
        capa_url=request.form.get('capa_url')
    )

    return redirect(url_for('livro.lista_livros'))