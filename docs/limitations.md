# Scope and known limitations

## Synthetic prototype

- Data provenance is documented as simulated in the internship report. Identifiers and monetary totals must not be presented as actual CNSS data or operational results.
- Data covers 2022-2024, with a stable simulated population. It does not model realistic hiring, departure or employer changes.
- Scenario outputs show the arithmetic effect of assumptions; they do not establish collection performance, causal effects, forecasts or benefit eligibility.
- Net balances can offset positive and negative employer-month balances. A portfolio of positive receivables requires a separate definition.

## Original dashboard presentation

The published screenshots deliberately preserve the original internship prototype:

- The overview date slider extends to September 2026, although the delivered observations end in December 2024.
- The overview contains a reference line labelled as a national CNSS average (94.7%). This is an illustrative workbook reference, not a verified national statistic in this repository.
- The employer screenshot has no single employer selected and shows multiple identity cards and aggregate indicators. Select an employer and verify filter propagation before interpreting it as one employer's situation.
- The employer screenshot displays a sector collection rate of 1596.3%. This is not a defensible portfolio collection ratio; the aggregation and filter context of this comparison require correction before it is used as a validated KPI. The CSV audit computes the overall ratio separately from summed paid and due amounts.
- Some labels in the scenario chart overlap. The underlying model and presentation would benefit from further review before production use.

No business-calculation changes have been made to the original workbook for this portfolio release. Local CSV path references were made relative and machine/author fingerprint attributes were removed from the shared copy. The embedded Hyper extract remains byte-identical to the original.

## Reproducibility boundary

Only the delivered workbook, four CSV files and original report images were available. Talend jobs, the supervisor's generator and Oracle source scripts are not included. The supplied validation script is a new portfolio utility, not an original internship deliverable.

The CSV validation checks structure and totals. It does not verify every embedded Hyper record, every Tableau calculation or the original execution of Talend jobs. Opening and visually testing the workbook in Tableau remains a separate check.
