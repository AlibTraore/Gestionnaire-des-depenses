
document.addEventListener('DOMContentLoaded', () => {
    console.log('Application chargée ✅');
    afficherSolde();
    modal();
    afficherHistorique();
});
const solde = document.getElementById('montant')
const popUp = document.querySelector('.popup-overlay')
const ajouter = document.getElementById('add')
document.getElementById('.reset')
const nameTitle = document.getElementById('text')
const nameNumber = document.getElementById('number')
const texteAction = document.querySelector('.popup-contenu h2')
async function afficherSolde() {
    try {
        const response = await fetch('/afficher')
        resultat = await response.json()
        solde.textContent = resultat.somme_Total

    } catch (error) {
        console.error("un probleme", error)
    }

};
function modal() {
    let mode = ''
    ajouter.addEventListener('click', () => {
        mode = 'ajouter'
        popUp.style.display = 'flex'
        console.log(popUp)
    })

    document.getElementById('retirer').addEventListener('click', () => {
        mode = 'retirer'
        texteAction.textContent = 'Retirer une depense'
        popUp.style.display = 'flex'
        console.log(mode)
    })

    // Un seul listener sur btnValider — pas de conflit !
    document.getElementById('btnValider').addEventListener('click', () => {
        if (mode === 'ajouter') {
            ajouterMontant()
        } else {

            console.log(popUp)
            retirerSolde()
        }
    })

    document.getElementById('btnFermer').addEventListener('click', () => {
        popUp.style.display = 'none'
        mode = ''
    })
}



async function ajouterMontant() {
    try {
        let response = await fetch('/ajouter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                champTitle: nameTitle.value,
                champNumber: +parseFloat(nameNumber.value)
            })
        });
        location.reload()
    } catch (error) {
        console.error("un probleme", error)
    }
}

async function afficherHistorique() {
    try {
        const response = await fetch("/historique")
        resultat = await response.json()
        table = document.querySelector('.historique table')

        for (let element of resultat) {
            const ligne = table.insertRow();
            const cellId = ligne.insertCell(0);
            const cellTitre = ligne.insertCell(1);
            const cellMontant = ligne.insertCell(2);
            const cellDate = ligne.insertCell(3);
            const cellDelete = ligne.insertCell(4);

            cellId.textContent = element.id;
            cellTitre.textContent = element.titre;
            if (element.montant < 0) {
                cellMontant.innerHTML = `<span style="color:#e74c3c">${element.montant} $</span>`;
            } else {
                cellMontant.innerHTML = `<span style="color:#2ecc71">+${element.montant} $</span>`;
            }
            cellDate.textContent = element.date;
            cellDelete.innerHTML = `<button class='btn-supprimer' onclick = 'retirerSomme(${element.id})'>🗑️</button>`;
        }
    } catch (error) {
        console.error('un probleme', error)
    }

}


async function retirerSolde() {

    try {
        const response = await fetch("/retirerSolde", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                champTitle: nameTitle.value,
                champNumber: -parseFloat(nameNumber.value)

            })

        });
        console.log(nameNumber.value)

    } catch (error) {
        console.log("un probleme", error)
    }
}

async function retirerSomme(element) {
    let idSupp = element
    try {
        const response = await fetch("/supprimer", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                idTable: idSupp
            })
        });
        const resultat = await response.json();
        document.getElementById('resultat-supp').textContent = resultat.resultat
        location.reload();

    } catch (error) {
        console.log("un probleme", error)
    }
}
console.log()
