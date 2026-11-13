# Sources de données — état du projet

## Football : API-Football
Le connecteur `data_sources/football_api.py` prévoit :
- calendrier du jour (`fixtures`)
- statistiques d'un match (`fixtures/statistics`)
- événements (`fixtures/events`)
- compositions (`fixtures/lineups`)

Une clé API-Football est requise. Créer un compte chez le fournisseur, copier la clé
dans `.env` sous `API_FOOTBALL_KEY=...`. Ne jamais publier `.env` sur GitHub.

Les quotas et compétitions accessibles dépendent de l'abonnement du fournisseur.
Le connecteur ne prétend pas que toutes les compétitions ou statistiques sont incluses.

## NHL : API publique NHL
Le connecteur `data_sources/nhl_api.py` interroge le scoreboard actuel et les statistiques
de club via l'API web publique NHL. Cette interface peut évoluer ; les réponses doivent
être validées avant tout calcul.

## Cotes Betclic
Aucune connexion officielle aux cotes Betclic n'est incluse dans cette version.
Saisir ou importer uniquement les cotes réellement visibles dans le compte Betclic.
Ne pas automatiser l'accès au compte ni contourner ses protections.

## Règle anti-invention
Une donnée absente doit rester absente. Chaque analyse future devra conserver :
- fournisseur
- horodatage de récupération
- identifiant du match/joueur
- champs manquants
- statut de validation
