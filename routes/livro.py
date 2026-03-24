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
    if arquivo and arquivo.filename != '':
        filename = secure_filename(arquivo.filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        caminho = os.path.join(UPLOAD_FOLDER, filename)
        arquivo.save(caminho)
        capa_url = '/' + caminho

    Livro.create(
        titulo=request.form.get('titulo'),
        autor=request.form.get('autor'),
        sinopse=request.form.get('descricao'), 
        capa_url=capa_url
    )
    return redirect(url_for('livro.lista_livros'))

@livro_route.route('/salvar', methods=['POST'])
def salvar_livro_json():
    capa_url = request.form.get('capa_url')
    
    arquivo = request.files.get('file_upload')
    if arquivo and arquivo.filename != '':
        filename = secure_filename(arquivo.filename)
      
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        
        caminho_no_disco = os.path.join(UPLOAD_FOLDER, filename)
        arquivo.save(caminho_no_disco)
        
        capa_url = '/static/uploads/capas/' + filename

    Livro.create(
        titulo=request.form.get('titulo'),
        autor=request.form.get('autor'),
        sinopse=request.form.get('descricao'), 
        capa_url=capa_url
    )
    return redirect(url_for('livro.lista_livros'))