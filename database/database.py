# database/models/usuario.py
# MODELO DE USUÁRIO: Define os campos da tabela 'usuario' 
# (Nome, Email, Senha Hash) para o ORM Peewee.

from peewee import MySQLDatabase
import os
from dotenv import load_dotenv

load_dotenv()

db = MySQLDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    # MUITO IMPORTANTE:
    charset='utf8mb4'
)