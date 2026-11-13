# Ligne Chance Pro AI

Premier socle Python pour développer simultanément les modules Football et NHL.

## Couverture prévue

### Football
- Résultat : 1X2, double chance, remboursé si nul, handicaps
- Buts : over/under, BTTS, total d'équipe, score exact
- Mi-temps : résultat, buts, mi-temps/fin
- Joueurs : buteur, passeur, tirs, tirs cadrés, passes
- Statistiques : corners, cartons, fautes, hors-jeu, possession

### NHL
- Buteur
- Passeur
- Tirs au but des joueurs

## Installation
Python 3.10 ou plus récent recommandé.

```bash
pip install -r requirements.txt
python main.py
```

## Important : intégrité des données
Cette version est un socle de calcul, pas encore un service de données en direct.
Elle ne télécharge pas automatiquement les matchs, blessures, compositions ou cotes Betclic.
Les probabilités doivent provenir d'une analyse documentée et les cotes doivent être
relevées sur Betclic au moment de l'analyse. Ne jamais remplacer une donnée manquante
par une valeur inventée.

## Prochaine étape technique
Connecter des fournisseurs de données fiables pour les calendriers, résultats,
statistiques, disponibilités et gardiens NHL, puis ajouter l'import des cotes
et la génération de rapports complets.


## Connecteurs de données (version 2)
- Football : connecteur API-Football, clé requise.
- NHL : connecteur vers l'API web publique NHL.
- Cotes Betclic : pas de connexion officielle automatique incluse ; seules les cotes observées et vérifiées doivent être utilisées.

Copier `.env.example` vers `.env`, puis renseigner la clé API-Football si disponible.
Voir `docs/DATA_SOURCES.md` pour les limites et règles de fiabilité.
