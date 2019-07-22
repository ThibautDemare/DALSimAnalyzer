# DALSimAnalyzer

Ce repo contient plusieurs scripts permettant de faciliter l'extraction, la fusion et l'analyse des résultats issus de 8 simulations exécutées sur le serveur. Ce nombre 8 vient du fait qu'on suppose qu'il n'y a eu que 8 simulations lancées en parallèles puisque le serveur ne dispose que de 8 cores. Néanmoins cela peut être adapté en fonction des besoins.

## Utilisation

### Récupération des données

Tout d'abords, il faut récupérer les données. On peut le faire grâce au script `extract.py`. Ce script télécharge l'ensemble des dossiers CSV des exécutions depuis le serveur sur lequel elles ont été lancées.

Pour lancer `extract.py`, il est nécessaire de configurer correctement le fichier `server_access_infos.py` avec le bon `username` et le bon `servername`. Il est également nécessaire d'avoir déployé sa clé publique ssh sur le serveur dans `~/.ssh/authorized_keys`.

Le script `extract.py` prend deux arguments en paramètre :
- le premier spécifie le dossier dans lequel se trouvent les simulations sur le serveur (les simulations sont elles-mêmes dans des sous-répertoires sous la forme `run1 run2 ...`).
- le deuxième permet d'indiquer le nombre de simulation qu'il faut récupérer.

Par exemple :

```
python extract.py ~/myfolder 8
```

### Fusion des fichiers CSV

La fusion s'effectue grâce à deux scripts possibles : `merge.py` et `merge_pandas.py`. La fusion consiste à calculer les moyennes de l'ensemble des cellules des fichiers CSV des simulations.
Le script génère les fichiers CSV fusionnés à partir des fichiers extraits précédemment et stockés dans `Results`. Les CSV fusionnés sont eux-même stocker dans le dossier `averageResults` ou `averageResults-pandas`.

On propose deux méthodes car la version utilisant Pandas permet de fusionné plus facilement un nombre varaible de simulations qui ont elles-même été éxecuté sur un un nombre d'étapes différentes. Nénamoins, l'ancienne méthode permet de fusionner les fichiers `distribution_nb_FC_per_LSP` que ne permet pas Pandas (pour le moment).

### Analyse

L'analyse est facilitée grâce au script `analyze.py`. Celui-ci génère des graphiques à partir des fichiers CSV fusionnés. Il récupère les fichiers fusionnés depuis le répertoire `averageResults-pandas` et enregistre chaque graphique dans le répertoire `Charts-pandas`.



