-- ===== Base de données : Portefeuille de Dépenses =====

CREATE TABLE IF NOT EXISTS depenses (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    titre     TEXT    NOT NULL,
    montant   REAL    NOT NULL,
    categorie TEXT,
    date      TEXT    
);
