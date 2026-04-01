import datetime
from peewee import Model, TextField, DateTimeField, ForeignKeyField
from database.models.usuario import Usuario
from database.models.clube import Clube

class Mensagem(Model):
    usuario = ForeignKeyField(Usuario)
    clube = ForeignKeyField(Clube, backref='mensagens')

    texto = TextField()
    data = DateTimeField(default=datetime.datetime.now)