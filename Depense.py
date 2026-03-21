import html
import flask
from flask import Flask, request, redirect, url_for
import io
import base64

import matplotlib.pyplot as plt

app = Flask(__name__)

categories=[
    {"tache":"Nourriture","montant":0},
    {"tache":"Transport","montant":0},
    {"tache":"Loisir","montant":0}
]


#commencons par l intrerface du choix
@app.route("/")
def accueil():
    html=''
    html += """
    <style>
    body{
    font-family: Arial, sans-serif;
    padding: 20px;

    }
    label{
        color:black;
        padding-top:100px;
    }

    button{
        margin-top:10px;
        color:white;
        padding:5px 10px;
        border: 10 px;
        background-color:grey;
        border-radius:3px

    }
    h1{
        font-size:20px;
        color:blue;
    }

    </style>
    <h1>MON PORTEFEUILLE</h1>
    <form method="post" action="/ajouter">
        <div>
            <label>Montant</label>
            <input type='number' name='montant' placeholder='Entrer un montant' required>
        </div>

        <div>
            <label>Catégorie</label>
            <select name='categorie' required>
                <option value=''>Choisir une catégorie</option>
                <option value='0'>Nourriture</option>
                <option value='1'>Transport</option>
                <option value='2'>Loisir</option>
            </select>
        </div>
        <button type='submit'>Ajouter</button>
    </form>
    <hr>
    """
    html+=f"<h1>CATEGORIES</h1>"
    html+="<hr>"
    html += "<ul style='list-style:none; padding:0;'>"
    total=0
    error=request.args.get('error','')
    image = generer_graphe()

    html+=f"{error}"
    for id,categorie in enumerate(categories,1):
        element=categorie["tache"]
        valeur=categorie["montant"]
        total+=categorie["montant"]
        html+=f"<ul style='color:black; text-decoration:none;'>{element}:{valeur} FCFA <a style='margin-left:20px' a href='/reset/{id}'>Remise a zero</a></ul> "
        
    html+=f"<h3 style='color:red; margin-left:35px;'>Total={total}</h3>"
    html+= f"<img src='data:image/png;base64,{image}'>"
    return html

@app.route('/ajouter', methods=['POST'])
def ajouter():
    try:
        montant = int(request.form.get('montant'))
        if montant <=0:
            
            return redirect(url_for('accueil',error= "montant nul"))
        if montant>100000:
            
            return redirect(url_for('accueil',error ="erreur d'entrerrr"))
        categorie=request.form.get('categorie')
        categories[int(categorie)]["montant"] += int(montant)
        return redirect(url_for('accueil'))
    except (ValueError, TypeError):
        return "erreur d entrer"

@app.route("/reset/<int:id>")
def reset(id):
    categories[id-1]["montant"]=0

    return redirect(url_for("accueil"))
    

@app.route("/",methods=['POST'])
def generer_graphe():
    import matplotlib.pyplot as plt
    import io, base64
    x = []
    y = ["jan","fev","mars","avril"]
    montants = int(request.form.get('montant'))
    x.append(montants)

    
    labels=y
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker="o")
    plt.title("Graphique personnalisé")
    plt.yticks(y, labels)
    plt.xlabel("Mois")
    plt.ylabel("Valeur")
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return base64.b64encode(buffer.getvalue()).decode("utf-8")
   
    
    

if __name__== '__main__':
   app.run(debug=True)