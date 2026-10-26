#Lab 4: Database-Driven Feature Table

## Project Overview

This project uses a SQLite database containing 566 patients from the TCGA Lung Adenocarcinoma PanCancer Atlas study. The goal is to explore a relational database, write SQL queries, and use Python to construct a patient-level feature table.

The final dataset contains one row per patient, including clinical characteristics, tumor mutation burden, and counts of protein-altering mutations for five genes: TP53, KRAS, EGFR, STK11, and KEAP1.

## Database Structure

The database contains four related tables:

| Table | Number of Rows | Grain |
|---|---:|---|
| patients | 566 | One patient |
| samples | 566 | One tumor sample |
| genes | 17,756 | One gene |
| mutations | 200,789 | One recorded mutation |

The tables are connected using the following foreign keys:

- `samples.patient_id` references `patients.patient_id`.
- `mutations.sample_id` references `samples.sample_id`.
- `mutations.gene_symbol` references `genes.gene_symbol`.

A complete description of the schema is included in `schema.md`.

## SQL Queries

### Query 1: Mutation Counts

The first query counts non-Silent mutations in TP53, KRAS, EGFR, STK11, and KEAP1 for each patient.

**Expected rows:** Up to 2,830 patient–gene combinations (566 patients × 5 genes), before excluding combinations with no qualifying mutations.

**Actual rows:** 700.

The query returns fewer rows because patients without qualifying mutations in a particular gene are not included in the grouped results.

### Query 2: Tissue Source Site and Tumor Stage

The second query counts distinct patients by tissue source site and tumor stage.

**Expected rows:** One row per observed site–stage combination.

**Actual rows:** 142.

The output contains 142 observed combinations rather than 566 patient-level rows because patients are grouped by their tissue source site and stage.

## Feature Table Construction

The feature table was created using SQL queries and Python with pandas.

The script:

1. Retrieves patient characteristics and tumor sample information using a LEFT JOIN.
2. Counts qualifying mutations for each of the five genes.
3. Reshapes mutation counts into separate gene columns.
4. Merges the mutation features with the patient-level data.
5. Replaces absent qualifying mutation counts with zero.
6. Checks patient counts and duplicate patient IDs.
7. Exports the final table as a tab-separated file.

**Final output:** `feature_table.tsv`

- Rows: 566
- Columns: 11
- Unique patients: 566
- Duplicate patient IDs: 0

## Missing Data Handling

Missing clinical information was preserved rather than removing patients.

| Variable | Missing Values |
|---|---:|
| Sex | 52 |
| Age at diagnosis | 71 |
| Tumor stage | 54 |
| Tissue source site | 0 |
| Tumor mutation burden | 0 |

Patients without recorded qualifying mutations in a particular gene were assigned a mutation count of zero.

A total of 109 patients had no recorded qualifying mutations across the five selected genes.

The patient count remained 566 throughout the feature table construction process.

## Validation

A manual verification was performed for patient `TCGA-05-4382`.

The database contained two non-Silent EGFR mutations:

- Mutation ID 2635: Missense_Mutation
- Mutation ID 2636: Missense_Mutation

The final feature table also reported two EGFR mutations for this patient.

This confirmed that the mutation counts agreed with the original database for the checked patient.

## How to Run

### Requirements

- Python 3
- pandas
- SQLite (included with Python)
- `cohort.db`

### Instructions

Place `cohort.db` in the same directory as the Python scripts.

To explore the schema:

```bash
python explore_database.py
```

To run the SQL queries:

```bash
python run_queries.py
```

To build the final feature table:

```bash
python build_feature_table.py
```

To verify an individual mutation count:

```bash
python verify_counts.py
```

The feature table script produces `feature_table.tsv` in the project directory.

## Project Files

- `cohort.db` — Provided SQLite database.
- `queries.sql` — SQL queries for mutation counts and site–stage summaries.
- `explore_database.py` — Database schema exploration.
- `run_queries.py` — Runs the SQL queries.
- `build_feature_table.py` — Creates the final patient-level feature table.
- `verify_counts.py` — Verifies an individual patient's mutation count.
- `feature_table.tsv` — Final dataset.
- `schema.md` — Database schema description.
- `data_dictionary.md` — Description of the final dataset columns.
- `AI_USAGE.md` — Documentation of AI assistance and verification.

## Data Source

TCGA Lung Adenocarcinoma PanCancer Atlas study, accessed through cBioPortal and provided for PUBH 4201 Lab 4.
