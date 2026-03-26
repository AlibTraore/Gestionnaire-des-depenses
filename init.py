import os
import sqlite3

#document permettant d'initialiser la BD sqlite3
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'depenses.db')

conn =  sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open("database/depenses.sql", "r") as f:
    resultat = f.read()

cursor.executescript(resultat)

print("La base de données ecole.db a été créée et remplie avec succès !")

conn.commit()
conn.close()