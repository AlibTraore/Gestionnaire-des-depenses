import sqlite3
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ajouter",methods = ['POST'])
def ajouterDepense():
    donnee =  request.get_json()
    titre = donnee.get('champTitle')
    montant =  donnee.get('champNumber')
    conn =  sqlite3.connect('depenses.db')
    conn.row_factory = sqlite3.Row
    cursor =  conn.cursor()
    cursor.execute("INSERT INTO depenses (titre,montant) VALUES (?,?)",(titre,montant))
    conn.commit()
    conn.close()
    return  jsonify({"message": "Dépense ajoutée !"})

@app.route('/afficher', methods = ['GET'])
def afficherSolde():
    conn =  sqlite3.connect('depenses.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultat = cursor.execute("SELECT montant FROM depenses").fetchall()
    dict_res = [dict (element) for element in resultat]
    totale = 0
    for amount in dict_res:
        totale = amount['montant'] + totale
    data = totale
    print(data) # Affiche les résultats dans le terminal
    conn.close()
    return jsonify({"somme_Total":data})
    
@app.route('/historique', methods = ['GET']) 
def afficherDepense():
    conn =  sqlite3.connect('depenses.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultat = cursor.execute("SELECT * FROM depenses").fetchall()
    data = [dict (element) for element in resultat]
    print(data)
    conn.close()
    return jsonify(data)
@app.route('/supprimer', methods = ['POST'])
def supprimerSolde():
    donnee =  request.get_json()
    id_supp = donnee.get('idTable')
    conn =  sqlite3.connect('depenses.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultat = cursor.execute("DELETE FROM depenses WHERE id=?",(id_supp,)).fetchone()
    conn.commit()
    print(resultat)
    conn.close()
    return jsonify({"resultat":"supprimer avec succes"})
if __name__ == '__main__':
    app.run(debug=True)
