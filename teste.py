from database.database import db
try:
    db.connect()
    print("CONECTOU NO MYSQL COM SUCESSO! ✅")
except Exception as e:
    print(f"ERRO DE CONEXÃO: {e} ❌")