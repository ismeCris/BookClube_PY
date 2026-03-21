from peewee import Model, CharField, TextField, DateTimeField
from database.database import db
import datetime

class Clube(Model):
    nome = CharField()
    descricao = TextField(null=True)

    data_criacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db