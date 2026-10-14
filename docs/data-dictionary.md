# Data dictionary

All rows are synthetic. Monetary fields are denominated in MAD. Identifiers should be read as strings to retain prefixes and leading zeros.

## Employer dimension - tableau_aff.csv

| Field | Meaning |
| --- | --- |
| AFF_NUM | Synthetic employer identifier; unique in this file |
| DATE_AFFILIATION | Simulated affiliation date |
| SECTEUR_ID / LIBELLE_SECTEUR | Sector identifier and label |
| REGION_ID / LIBELLE_REGION | Region identifier and label |
| VILLE_ID / LIBELLE_VILLE | City identifier and label |

## Calendar dimension - tableau_cal.csv

| Field | Meaning |
| --- | --- |
| PERIODE | Monthly key, YYYYMM |
| ANNEE / MOIS | Year and month |
| TRIMESTRE / SEMESTRE | Quarter and half-year |
| NOM_MOIS | Month label |
| DATE_DEBUT / DATE_FIN | Calendar boundaries |

## Contribution facts - tableau_payment.csv

Unique key: AFF_NUM + PERIODE.

| Field | Meaning in the workbook |
| --- | --- |
| AFF_NUM / PERIODE | Employer and calendar references |
| DEBIT_CNSS / DEBIT_AMO / DEBIT_TFP | Contributions due by component |
| CREDIT_CNSS / CREDIT_TFP | Contribution payments used in the paid measure |
| PN_CNSS / PN_TFP | Recorded penalties |

## Payroll facts - tableau_salaires.csv

Unique key: AFF_NUM + IMMA_NUM + PERIODE.

| Field | Meaning |
| --- | --- |
| AFF_NUM | Employer reference |
| IMMA_NUM | Synthetic insured identifier |
| PERIODE | Monthly calendar reference |
| SALAIRE_BRUT | Declared monthly gross salary, MAD |

## Aggregation rules

Contribution and payroll facts have different grains. Do not physically join them and then sum contribution values without first controlling the grain; each contribution could be repeated for every payroll declaration.

Count distinct IMMA_NUM values for people, and count rows for monthly declarations. Calculate the collection ratio from aggregate paid and due amounts rather than summing employer percentages. The calendar appears twice in the original Tableau logical model, so time-filter propagation must be reviewed across sheets.
