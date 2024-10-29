# 🚛 Calculateur de Besoins en Camions

## Description
Cette application Streamlit permet de calculer le nombre de camions (semi-remorques et porteurs) nécessaires pour transporter un nombre donné de palettes, en prenant en compte différents types de palettes et contraintes logistiques.

## Fonctionnalités

### Types de Palettes Supportés
- Palettes Europe (80 x 120 cm)
- Palettes Industrielles (100 x 120 cm)
- Demi-palettes (80 x 60 cm)

### Capacités des Véhicules

#### Semi-remorque (13,6 mètres)
- 33 Palettes Europe (32 avec espace chariot)
- 26 Palettes Industrielles (25 avec espace chariot)
- Possibilité de double empilage

#### Porteur 7,5 mètres
- 19 Palettes Europe (18 avec espace chariot)
- 14 Palettes Industrielles (13 avec espace chariot)

#### Porteur 9 mètres
- 22 Palettes Europe (21 avec espace chariot)
- 18 Palettes Industrielles (17 avec espace chariot)

### Options d'Export
- Excel (.xlsx)
- CSV
- HTML (compatible PDF)

## Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone [URL_DU_REPO]
cd calculateur-camions
```

2. Créez un environnement virtuel (recommandé) :
```bash
python -m venv venv
source venv/bin/activate  # Pour Linux/Mac
# ou
venv\Scripts\activate  # Pour Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancez l'application :
```bash
streamlit run app.py
```

2. Ouvrez votre navigateur à l'adresse indiquée (généralement `http://localhost:8501`)

3. Remplissez les champs requis :
   - Nombre de palettes de chaque type
   - Cochez l'option double empilage si nécessaire
   - Indiquez le nombre de livraisons à répartir

4. Cliquez sur "Calculer les besoins"

5. Consultez les résultats et utilisez les boutons d'export selon vos besoins

## Structure du Projet
```
calculateur-camions/
│
├── app.py              # Application principale
├── requirements.txt    # Dépendances Python
└── README.md          # Ce fichier
```

## Dépendances
- streamlit
- pandas
- xlsxwriter

## Fichier Requirements.txt
Créez un fichier `requirements.txt` avec le contenu suivant :
```
streamlit
pandas
xlsxwriter
```

## Notes Importantes
- Un espace équivalent à une demi-palette est automatiquement réservé pour le chariot élévateur dans chaque véhicule
- Les calculs prennent en compte les contraintes de poids et d'espace
- En cas de double empilage, la capacité des semi-remorques est doublée

## Contribution
Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Support
En cas de problème ou pour des suggestions d'amélioration :
1. Ouvrez une issue dans le dépôt GitHub
2. Décrivez précisément le problème rencontré
3. Ajoutez les logs d'erreur si applicable

## Licence
Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.