from peewee import Model, CharField, TextField, DateTimeField, ForeignKeyField, BooleanField, IntegerField
from database.database import db
from database.models.usuario import Usuario
import datetime

class Clube(Model):
    nome = CharField()
    descricao = TextField(null=True)

    dono = ForeignKeyField(Usuario, backref='clubes_criados')
    
    # Novos campos solicitados
    senha = CharField(null=True) # Se houver senha, tratamos como privado
    publico = BooleanField(default=True) # True = Aberto, False = Restrito
    limite_membros = IntegerField(default=0) # 0 para ilimitado
    
    data_criacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db