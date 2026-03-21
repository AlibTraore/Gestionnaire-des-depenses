import os
import sqlite3


conn =  sqlite3.connect('depenses.db')
cursor = conn.cursor()

with open("database/depenses.sql", "r") as f:
    resultat = f.read()

cursor.executescript(resultat)

print("La base de données ecole.db a été créée et remplie avec succès !")

conn.commit()
conn.close()