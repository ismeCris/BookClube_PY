from peewee import Model, CharField, DateTimeField, IntegerField,TextField
from database.database import db
import datetime

class Livro(Model):
    
    titulo = CharField()
    autor = CharField()
    editora = CharField()
    num_pag = IntegerField()
    genero = CharField()
    sinopse = TextField()
    
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

