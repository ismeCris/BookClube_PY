from peewee import Model, CharField, DateTimeField, IntegerField, TextField
from database.database import db
import datetime

class Livro(Model):
    titulo = CharField()
    autor = CharField()
    editora = CharField(null=True)
    num_pag = IntegerField(null=True)
    genero = CharField(null=True)
    sinopse = TextField(null=True)
    capa_url = CharField(null=True)

    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db