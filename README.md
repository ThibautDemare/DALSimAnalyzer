# DALSimAnalyzer

Ce repo contient plusieurs scripts permettant de faciliter l'extraction, la fusion et l'analyse des résultats issus de 8 simulations exécutées sur le serveur. Ce nombre 8 vient du fait qu'on suppose qu'il n'y a eu que 8 simulations lancées en parallèles puisque le serveur ne dispose que de 8 cores. Néanmoins cela peut être adapté en fonction des besoins.

## Utilisation

### Récupération des données

Tout d'abords, il faut récupérer les données. On peut le faire grâce au script `extract.py`. Ce script télécharge l'ensemble des dossiers CSV des 1 à 8 exécutions depuis le serveur sur lequel elles ont été lancées.

Pour lancer `extract.py`, il est nécessaire de configurer correctement le fichier `server_access_infos.py` avec le bon `username` et le bon `servername`. Il est également nécessaire d'avoir déployé sa clé publique ssh sur le serveur dans `~/.ssh/authorized_keys`.

D'autre part, vous pouvez aussi mettre à jour le fichier `extract.py` (notamment ligne 15) en spécifiant l'arborescence dans laquelle se trouve les dossiers `run` des simulations.

### Fusion des fichiers CSV

La fusion s'effectue grâce au script `merge.py`. La fusion consiste à calculer les moyennes de l'ensemble des cellules des fichiers CSV des 8 simulations.
Le script génère les fichiers CSV fusionnés dans le dossier `averageResults`  et à partir des fichiers extraits précédemment et stockés dans `Results`.

### Analyse

TODO

L'analyse est facilitée grâce au script `analyze.py`. Celui-ci génère des graphiques à partir des fichiers CSV fusionnés.



