from flask import Blueprint, render_template, request, redirect, url_for
from database.models.livro import Livro
from werkzeug.utils import secure_filename
import os

livro_route = Blueprint('livro', __name__)
UPLOAD_FOLDER = 'static/uploads/capas'

@livro_route.route('/')
def lista_livros():
    todos_os_livros = Livro.select()
    return render_template('livros.html', livros=todos_os_livros)

@livro_route.route('/salvar', methods=['POST'])
def salvar_livro():
    capa_url = request.form.get('capa_url')

    arquivo = request.files.get('file_upload')

    # 👉 PRIORIDADE: arquivo do PC
    if arquivo and arquivo.filename != '':
        filename = secure_filename(arquivo.filename)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        caminho = os.path.join(UPLOAD_FOLDER, filename)
        arquivo.save(caminho)

        capa_url = '/static/uploads/capas/' + filename

    if not capa_url:
        capa_url = '/static/images/minha_capa_padrao.jpg'

    Livro.create(
        titulo=request.form.get('titulo'),
        autor=request.form.get('autor'),
        sinopse=request.form.get('descricao'),
        capa_url=capa_url
    )

    return redirect(url_for('livro.lista_livros'))

@livro_route.route('/<int:id>/editar', methods=['POST'])
def editar_livro(id):
    livro = Livro.get_by_id(id)

    capa_url = request.form.get('capa_url')
    arquivo = request.files.get('file_upload')

    # Se enviou nova imagem
    if arquivo and arquivo.filename != '':
        filename = secure_filename(arquivo.filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        caminho = os.path.join(UPLOAD_FOLDER, filename)
        arquivo.save(caminho)

        capa_url = '/static/uploads/capas/' + filename

    # Atualiza os dados
    livro.titulo = request.form.get('titulo')
    livro.autor = request.form.get('autor')
    livro.sinopse = request.form.get('descricao')

    if capa_url:
        livro.capa_url = capa_url

    livro.save()

    return redirect(url_for('livro.lista_livros'))