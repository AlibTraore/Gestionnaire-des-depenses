
document.addEventListener('DOMContentLoaded', () => {
    console.log('Application chargée ✅');
    afficherSolde();
    modal()
    fermerModal()
    envoyerModal()
    afficherHistorique();
});
const solde = document.getElementById('montant')
const popUp = document.querySelector('.popup-overlay')
const ajouter = document.getElementById('add')
document.getElementById('.reset')

const nameTitle = document.getElementById('text')
const nameNumber = document.getElementById('number')

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
    ajouter.addEventListener('click', () => {
        popUp.style.display = 'flex'
        console.log(popUp)
    })
}
function fermerModal() {
    document.getElementById('btnFermer').addEventListener('click', () => {
        popUp.style.display = 'none'
    })
}
function envoyerModal() {
    document.getElementById('btnValider').addEventListener('click', () => {
        ajouterMontant()
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
                champNumber: nameNumber.value
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
            cellMontant.innerHTML = `${element.montant} $`;
            cellDelete.innerHTML = `<button class='btn-supprimer' onclick = 'retirerSomme(${element.id})'>🗑️</button>`;
        }
    } catch (error) {
        console.error('un probleme', error)
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
        location.reload()
    } catch (error) {
        console.log("un probleme", error)
    }
}
console.log()
