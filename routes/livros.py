from flask import blueprint

home_route = blueprint('Cad_livro',__name__)

@home_route.route('/')
def livros():
    pass