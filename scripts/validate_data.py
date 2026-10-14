"""Validate the delivered synthetic CSV datasets using only Python's standard library."""
import csv
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def rows(name):
    with (ROOT / 'data' / name).open(encoding='utf-8-sig', newline='') as stream:
        yield from csv.DictReader(stream)

def inspect(name, keys):
    seen = set()
    count = missing = duplicates = 0
    for row in rows(name):
        count += 1
        missing += sum(value is None or value == '' for value in row.values())
        key = tuple(row[k] for k in keys)
        duplicates += key in seen
        seen.add(key)
    return {'rows': count, 'missing_cells': missing, 'duplicate_keys': duplicates}

def main():
    specs = {
        'tableau_aff.csv': ['AFF_NUM'],
        'tableau_cal.csv': ['PERIODE'],
        'tableau_payment.csv': ['AFF_NUM', 'PERIODE'],
        'tableau_salaires.csv': ['AFF_NUM', 'IMMA_NUM', 'PERIODE'],
    }
    tables = {name: inspect(name, keys) for name, keys in specs.items()}
    employers = {r['AFF_NUM'] for r in rows('tableau_aff.csv')}
    periods = {r['PERIODE'] for r in rows('tableau_cal.csv')}
    orphan_employers = orphan_periods = negative_salaries = 0
    insured = set()
    by_month = Counter()
    due = paid = penalties = Decimal(0)
    for row in rows('tableau_payment.csv'):
        orphan_employers += row['AFF_NUM'] not in employers
        orphan_periods += row['PERIODE'] not in periods
        due += sum((Decimal(row[k]) for k in ['DEBIT_CNSS', 'DEBIT_AMO', 'DEBIT_TFP']), Decimal(0))
        paid += sum((Decimal(row[k]) for k in ['CREDIT_CNSS', 'CREDIT_TFP']), Decimal(0))
        penalties += Decimal(row['PN_CNSS']) + Decimal(row['PN_TFP'])
    for row in rows('tableau_salaires.csv'):
        orphan_employers += row['AFF_NUM'] not in employers
        orphan_periods += row['PERIODE'] not in periods
        negative_salaries += Decimal(row['SALAIRE_BRUT']) < 0
        insured.add(row['IMMA_NUM'])
        by_month[row['PERIODE']] += 1
    result = {
        'data_origin': 'Synthetic data, as documented in the internship report; not official CNSS statistics.',
        'tables': tables,
        'distinct_employers': len(employers), 'distinct_insured_identifiers': len(insured),
        'period_start': min(periods), 'period_end': max(periods), 'monthly_periods': len(periods),
        'orphan_employer_references': orphan_employers, 'orphan_period_references': orphan_periods,
        'negative_gross_salaries': negative_salaries,
        'payroll_rows_per_month': dict(sorted(by_month.items())),
        'metrics_MAD': {
            'contributions_due_including_AMO': str(due), 'contributions_paid': str(paid),
            'penalties': str(penalties), 'net_outstanding_including_penalties': str(due + penalties - paid),
            'collection_ratio_percent': str((paid / due * 100).quantize(Decimal('0.01'))),
        },
    }
    issues = sum(t['missing_cells'] + t['duplicate_keys'] for t in tables.values())
    issues += orphan_employers + orphan_periods + negative_salaries
    result['structural_checks_passed'] = issues == 0
    (ROOT / 'docs/validation.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))
    if issues:
        raise SystemExit('Data validation found structural issues; review docs/validation.json.')

if __name__ == '__main__':
    main()
