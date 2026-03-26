from peewee import Model, CharField, DateTimeField, IntegerField, TextField, ForeignKeyField, BooleanField
from database.database import db
from datetime import datetime
from database.models.usuario import Usuario

class Livro(Model):
    STATUS_EXPLORAR = 'explorar'
    STATUS_LIDO = 'lido'
    STATUS_FAVORITO = 'favorito'

    titulo = CharField()
    autor = CharField()
    editora = CharField(null=True)
    num_paginas = IntegerField(null=True)
    genero = CharField(null=True)
    sinopse = TextField(null=True)
    capa_url = CharField(null=True)

    status = CharField(default=STATUS_EXPLORAR)
    usuario = ForeignKeyField(Usuario, backref='livros')

    avaliacao = IntegerField(default=0)
    favorito = BooleanField(default=False)

    data_registro = DateTimeField(default=datetime.now)

    class Meta:
        database = db