from peewee import Model, CharField, DateTimeField, TextField
from database.database import db
import datetime

class Usuario(Model):
    # Dados para Cadastro
    nome = CharField()
    email = CharField(unique=True)  # unique=True impede e-mails repetidos
    senha = CharField()            # Aqui vai o hash da senha
    
    telefone = CharField(null=True) # null=True se não for obrigatório
    endereco = TextField(null=True)
    
    # Controle do sistema
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db