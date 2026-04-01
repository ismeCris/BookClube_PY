import datetime
from peewee import Model, CharField, ForeignKeyField
from database.models.clube import Clube


class LivroClube(Model):
    clube = ForeignKeyField(Clube, backref='livros')
    titulo = CharField()
    autor = CharField()

    mes_referencia = CharField()  # ex: "03/2026"