# Tableau de bord BI — Cotisations et déclarations salariales

[English](README.md) · [Français](README.fr.md) · [Documentation](docs/README.md)

Projet individuel réalisé par **Yassine Khadir** pendant un stage d’un mois à la **CNSS, Casablanca, en septembre 2026**. Il présente une démarche de business intelligence, de l’intégration des données à leur exploration dans Tableau.

> Toutes les données sont simulées. Ce dépôt ne contient pas de dossiers réels d’employeurs ou d’assurés et ne constitue ni une publication officielle de la CNSS, ni un système de production. Les scénarios sont des simulations arithmétiques, pas des prévisions validées.

![Vue d’ensemble — données simulées](docs/images/overview.png)

## Objectif et contribution

Le projet organise des cotisations et des déclarations salariales pour explorer des indicateurs, comparer des territoires et des secteurs, et simuler des hypothèses de recouvrement.

Mon travail a porté sur l’intégration avec **Talend Open Studio**, le stockage sous **Oracle SQL**, la modélisation analytique et la création de **trois tableaux de bord Tableau Public**. Le script Python de génération des données a été fourni par mon encadrant.

## Données disponibles

Les observations couvrent **janvier 2022 à décembre 2024**. Cette période est distincte de celle du stage.

| Fichier | Lignes | Niveau de détail |
| --- | ---: | --- |
| `data/tableau_aff.csv` | 500 | Un employeur simulé |
| `data/tableau_cal.csv` | 36 | Un mois |
| `data/tableau_payment.csv` | 18 000 | Un employeur et un mois |
| `data/tableau_salaires.csv` | 836 244 | Un employeur, un identifiant d’assuré et un mois |

Le jeu comprend **23 229 identifiants d’assurés simulés**. Le [dictionnaire des données](docs/data-dictionary.md) précise les champs et les règles d’agrégation. Les faits de cotisation et de salaire ont des niveaux de détail différents : une jointure directe peut multiplier les montants de cotisation.

## Les trois tableaux de bord

1. **Vue d’ensemble** : cotisations dues et payées, pénalités, solde net, taux de recouvrement et tendances régionales.
2. **Analyse employeur et territoire** : effectifs, masse salariale, historique et comparaisons sectorielles. Sélectionner un employeur avant d’interpréter les indicateurs individuels.
3. **Scénarios de recouvrement** : hypothèses de récupération des soldes et de remise partielle des pénalités.

![Analyse employeur — état initial sans sélection unique](docs/images/employer-analysis.png)

![Scénarios sur données simulées](docs/images/collection-scenarios.png)

Les images proviennent du rapport de stage et conservent l’état du prototype. Certaines présentations restent à corriger : filtre de dates au-delà de 2024, référence nationale illustrative non vérifiée, taux sectoriel mal agrégé et chevauchements de libellés. Consulter les [limites détaillées](docs/limitations.md) avant toute interprétation.

## Ouvrir le projet

1. Télécharger le dépôt avec **Code → Download ZIP**, puis décompresser le dossier.
2. Ouvrir [tableau/cnss_dashboard.twbx](tableau/cnss_dashboard.twbx) dans une application Tableau compatible avec les classeurs empaquetés. Le fichier a été enregistré avec **Tableau 2026.2.2**.
3. Le classeur contient son extrait Hyper. Pour reconnecter ou actualiser les sources, sélectionner les CSV correspondants dans `data/`.
4. Parcourir les trois onglets et tester les filtres et paramètres.

GitHub affiche les captures, mais n’exécute pas le classeur Tableau dans le navigateur. Le fichier `.twb` est fourni pour consulter le modèle et les calculs.

## Vérifications reproductibles

Avec Python 3, depuis la racine du dépôt :

```sh
python scripts/validate_data.py
python scripts/check_repository.py
```

Aucun paquet supplémentaire n’est requis. Les contrôles portent sur les clés, les valeurs manquantes, les références, les salaires négatifs et les totaux financiers. Le [résultat publié](docs/validation.json) peut être régénéré. Le second script vérifie les empreintes des fichiers et les liens locaux de la documentation. Ces contrôles sont également exécutés par GitHub Actions.

## Périmètre et droits

Le dépôt contient les classeurs Tableau, quatre CSV, trois captures et la documentation. **Le générateur Python d’origine, les exports des jobs Talend et les scripts Oracle n’étaient pas présents dans le dossier fourni.** La chaîne ETL initiale ne peut donc pas être reconstruite intégralement à partir de ce dépôt. Les scripts de validation sont des utilitaires ajoutés pour le portfolio.

Les montants sont en MAD. Le taux de recouvrement est calculé à partir de la somme des montants payés divisée par la somme des montants dus. Les définitions utilisées sont détaillées dans le [README anglais](README.md).

Aucune licence de réutilisation n’a été attribuée aux livrables initiaux du stage. La visibilité publique n’accorde pas, à elle seule, de licence. Le nom CNSS situe le contexte du stage et n’implique pas d’approbation institutionnelle.

**Contact professionnel :** [Yassine Khadir sur LinkedIn](https://www.linkedin.com/in/yassine-khadir/).
