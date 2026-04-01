from peewee import Model, ForeignKeyField, CharField, DateTimeField
from database.database import db
from database.models.usuario import Usuario
from database.models.clube import Clube

class UsuarioClube(Model):
    usuario = ForeignKeyField(Usuario, backref='membros')
    clube = ForeignKeyField(Clube, backref='membros')

    status = CharField(default='pendente')
    data_entrada = DateTimeField(null=True)

    class Meta:
        database = db