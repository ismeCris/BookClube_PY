from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from database.models.clube import Clube
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from database.models.usuario_clube import UsuarioClube
clube_route = Blueprint('clube', __name__)

@clube_route.route('/')
def lista_clubes():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['usuario_id']
    meus_clubes = Clube.select().where(Clube.dono == user_id)
    clubes_participando = Clube.select().join(UsuarioClube).where(
        (UsuarioClube.usuario == user_id) & 
        (UsuarioClube.status == 'aprovado') &
        (Clube.dono != user_id)
    )
    vinculos_existentes = UsuarioClube.select(UsuarioClube.clube).where(UsuarioClube.usuario == user_id)
    explorar = Clube.select().where(
        (Clube.dono != user_id) & 
        (Clube.id.not_in(vinculos_existentes))
    )

    return render_template('clube.html', 
                           meus_clubes=meus_clubes, 
                           clubes_participando=clubes_participando,
                           explorar=explorar)


@clube_route.route('/<int:id>')
def ver_clube(id):
    clube = Clube.get_by_id(id)
    
    pendentes = UsuarioClube.select().where(
        (UsuarioClube.clube == clube) & 
        (UsuarioClube.status == 'pendente')
    )
 
    membros = UsuarioClube.select().where(
        (UsuarioClube.clube == clube) & 
        (UsuarioClube.status == 'aprovado')
    )

    return render_template('clube_detalhe.html', 
                           clube=clube, 
                           pendentes=pendentes, 
                           membros=membros)
@clube_route.route('/explorar')
def explorar_clubes():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))

    clubes = Clube.select().where(Clube.dono != session['usuario_id'])
    
    return render_template('explorar.html', clubes=clubes)


# CRIAR CLUBE
@clube_route.route('/criar', methods=['POST'])
def criar_clube():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    limite = request.form.get('limite_membros', 0)
    is_publico = request.form.get('publico') == "True"
    senha = request.form.get('senha')

    senha_hash = generate_password_hash(senha) if (not is_publico and senha) else None

    clube = Clube.create(
        nome=nome,
        descricao=descricao,
        limite_membros=int(limite),
        publico=is_publico,
        senha=senha_hash,
        dono=session['usuario_id']
    )

    UsuarioClube.create(
        usuario=session['usuario_id'],
        clube=clube,
        status='aprovado'
    )

    flash(f"Clube '{nome}' criado com sucesso!")
    return redirect(url_for('clube.lista_clubes'))

# DELETAR CLUBE
@clube_route.route('/<int:id>/deletar', methods=['POST'])
def deletar_clube(id):
    clube = Clube.get_by_id(id)

    if clube.dono.id != session.get('usuario_id'):
        flash("Sem permissão")
        return redirect(url_for('clube.lista_clubes'))

    clube.delete_instance()
    flash("Clube removido!")
    return redirect(url_for('clube.lista_clubes'))

@clube_route.route('/<int:id>/entrar', methods=['POST'])
def entrar_clube(id):
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))

    clube = Clube.get_by_id(id)
    senha = request.form.get('senha')

    if not clube.publico:
        if not senha or not check_password_hash(clube.senha, senha):
            flash("Senha incorreta para o clube privado!")
            return redirect(url_for('clube.lista_clubes'))
        status_inicial = 'pendente'
    else:
        status_inicial = 'aprovado'

    # Cria o vínculo
    UsuarioClube.create(
        usuario=session['usuario_id'],
        clube=clube,
        status=status_inicial
    )

    flash("Bem-vindo!" if status_inicial == 'aprovado' else "Solicitação enviada!")

    return redirect(url_for('clube.lista_clubes'))

@clube_route.route('/membro/<int:id>/aprovar', methods=['POST'])
def aprovar_membro(id):
    membro = UsuarioClube.get_by_id(id)

    if membro.clube.dono.id != session['usuario_id']:
        flash("Sem permissão")
        return redirect(url_for('clube.lista_clubes'))

    membro.status = 'aprovado'
    membro.save()

    flash("Membro aprovado!")
    return redirect(url_for('clube.ver_clube', id=membro.clube.id))

@clube_route.route('/<int:id>/editar', methods=['POST'])
def editar_clube(id):
    clube = Clube.get_by_id(id)

    if clube.dono.id != session['usuario_id']:
        flash("Sem permissão")
        return redirect(url_for('clube.lista_clubes'))

    clube.nome = request.form.get('nome')
    clube.descricao = request.form.get('descricao')
    clube.save()

    flash("Clube atualizado!")
    return redirect(url_for('clube.lista_clubes'))


