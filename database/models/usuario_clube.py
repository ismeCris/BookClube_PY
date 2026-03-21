from peewee import Model, ForeignKeyField
from database.database import db
from database.models.usuario import Usuario
from database.models.clube import Clube

class UsuarioClube(Model):
    usuario = ForeignKeyField(Usuario, backref='clubes')
    clube = ForeignKeyField(Clube, backref='usuarios')

    class Meta:
        database = db