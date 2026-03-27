from flask import Blueprint, render_template, request, redirect, url_for,session
from database.models.livro import Livro
from werkzeug.utils import secure_filename
import os
from werkzeug.utils import secure_filename

livro_route = Blueprint('livro', __name__)
UPLOAD_FOLDER = 'static/uploads/capas'

@livro_route.route('/')
def lista_livros():
    usuario_id = session.get('usuario_id')

    if not usuario_id:
        return redirect(url_for('usuario.login'))

    livros = Livro.select().where(Livro.usuario == usuario_id)

    return render_template('livros.html', livros=livros)

@livro_route.route('/salvar', methods=['POST'])
def salvar_livro():
    usuario_id = session.get('usuario_id')
    
    if not usuario_id:
        return redirect(url_for('usuario.login'))

    capa_url = request.form.get('capa_url')
    arquivo = request.files.get('file_upload')

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
        genero=request.form.get('genero'),
        status=request.form.get('status'),
        avaliacao=request.form.get('avaliacao') or None, 
        capa_url=capa_url,
        usuario=usuario_id
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
    livro.status = request.form.get('status')
    livro.genero = request.form.get('genero')
    livro.avaliacao = request.form.get('avaliacao')
    if capa_url:
        livro.capa_url = capa_url

    livro.save()

    return redirect(url_for('livro.lista_livros'))

@livro_route.route('/<int:id>/favoritar', methods=['POST'])
def favoritar(id):
    livro = Livro.get_by_id(id)
    livro.favorito = not livro.favorito
    livro.save()
    return redirect(url_for('livro.lista_livros'))