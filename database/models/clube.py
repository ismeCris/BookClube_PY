from peewee import Model, CharField, TextField, DateTimeField, ForeignKeyField
from database.database import db
from database.models.usuario import Usuario
import datetime

class Clube(Model):
    nome = CharField()
    descricao = TextField(null=True)

    dono = ForeignKeyField(Usuario, backref='clubes_criados')
    senha = CharField(null=True)

    data_criacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db