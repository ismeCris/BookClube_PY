
import datetime
from peewee import Model, TextField, DateTimeField, ForeignKeyField
from database.models.usuario import Usuario
from database.models.livroClube import LivroClube
from datetime import datetime


class Resenha(Model):
    usuario = ForeignKeyField(Usuario)
    livro = ForeignKeyField(LivroClube, backref='resenhas')

    texto = TextField()
    data = DateTimeField(default=datetime.datetime.now)