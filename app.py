import sqlite3
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'depenses.db')



@app.route('/')
def index():
    return render_template('index.html')

#fonction permettant d'ajouter des montant a notre gestionnaire
@app.route("/ajouter",methods = ['POST'])
def ajouterDepense():
    donnee =  request.get_json()
    titre = donnee.get('champTitle')
    montant = float(donnee.get('champNumber'))
    date_ajout = datetime.now().strftime("%Y-%m-%d")
    conn =  sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor =  conn.cursor()
    cursor.execute("INSERT INTO depenses (titre,montant,date) VALUES (?,?,?)",(titre,montant,date_ajout))
    conn.commit()
    conn.close()
    return  jsonify({"message": "Dépense ajoutée !"})

#fonction permettant d'afficher le solde principal
@app.route('/afficher', methods = ['GET'])
def afficherSolde():
    conn =  sqlite3.connect(DB_PATH)
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

#fonction qui affiche l'historique des ajouts et suppression dans le portfeuille
@app.route('/historique', methods = ['GET']) 
def afficherDepense():
    conn =  sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultat = cursor.execute("SELECT * FROM depenses").fetchall()
    data = [dict (element) for element in resultat]
    print(data)
    conn.close()
    return jsonify(data)
    
#function qui permet de supprimer depuis l'historique du portfeuille
@app.route('/supprimer', methods = ['POST'])
def supprimerSolde():
    donnee =  request.get_json()
    id_supp = donnee.get('idTable')
    conn =  sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultat = cursor.execute("DELETE FROM depenses WHERE id=?",(id_supp,)).fetchone()
    conn.commit()
    print(resultat)
    conn.close()
    return jsonify({"resultat":"supprimer avec succes"})

@app.route('/retirerSolde', methods = ['POST'])
def retirerSolde():
    donnee =  request.get_json()
    titre = donnee.get('champTitle')
    montant = float(donnee.get('champNumber'))
    date_ajout = datetime.now().strftime("%Y-%m-%d")
    conn =  sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor =  conn.cursor()
    cursor.execute("INSERT INTO depenses (titre,montant,date) VALUES (?,?,?)",(titre,montant,date_ajout))
    conn.commit()
    conn.close()
    return  jsonify({"message": "Dépense ajoutée !"})

if __name__ == '__main__':
    app.run(debug=True)
