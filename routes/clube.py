from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from database.models.clube import Clube

clube_route = Blueprint('clube', __name__)


# LISTAR CLUBES
@clube_route.route('/')
def lista_clubes():
    clubes = Clube.select()
    return render_template('clube.html', clubes=clubes)


# CRIAR CLUBE
@clube_route.route('/criar', methods=['POST'])
def criar_clube():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')

    if not nome:
        flash("Nome é obrigatório")
        return redirect(url_for('clube.lista_clubes'))

    Clube.create(
        nome=nome,
        descricao=descricao
    )

    flash("Clube criado com sucesso!")
    return redirect(url_for('clube.lista_clubes'))


# EDITAR CLUBE
@clube_route.route('/<int:id>/editar', methods=['POST'])
def editar_clube(id):
    clube = Clube.get_by_id(id)

    clube.nome = request.form.get('nome')
    clube.descricao = request.form.get('descricao')

    clube.save()

    flash("Clube atualizado!")
    return redirect(url_for('clube.lista_clubes'))


# DELETAR CLUBE
@clube_route.route('/<int:id>/deletar', methods=['POST'])
def deletar_clube(id):
    clube = Clube.get_by_id(id)
    clube.delete_instance()

    flash("Clube removido!")
    return redirect(url_for('clube.lista_clubes'))