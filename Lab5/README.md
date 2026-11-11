# Lab 5: Scalable Analysis Workflow

## Overview

This project uses Snakemake to automate a reproducible data analysis workflow using datasets and scripts from Labs 3 and 4.

The workflow cleans messy sample data, queries a patient database, combines the resulting datasets, and generates a summary report.

## Workflow Steps

1. **Data Cleaning:** Uses regex-based cleaning functions from Lab 3 to standardize sample IDs, patient names, dates of birth, sex, enrollment sites, and glucose measurements.
2. **Database Query:** Uses SQL and Python to extract patient information and mutation features from the Lab 4 database.
3. **Data Combination:** Combines the two datasets into a single table using pandas.
4. **Summary Report:** Produces a text report describing record counts, missing values, and the combined dataset.

## Dataset Information

- Lab 3: 60 sample records
- Lab 4: 566 patient records
- Combined dataset: 626 records

The two datasets have no matching patient identifiers. Therefore, they were concatenated rather than joined by patient ID. The resulting table preserves records from both datasets but does not represent matched patients.

## Requirements

- Python
- Snakemake
- pandas
- Conda (recommended for environment management)

## How to Run

Activate the environment containing Snakemake and pandas:

```bash
conda activate repro-demo
```

From the `Lab5` directory, run:

```bash
snakemake --cores 1
```

To preview the workflow without running any jobs:

```bash
snakemake -n --cores 1
```

To regenerate the results from a clean state, delete the generated outputs and rerun Snakemake:

```bash
rm -f results/cleaned_samples.csv results/feature_table.tsv results/combined_table.csv results/summary_report.txt
snakemake --cores 1
```

## Reproducibility Testing

**Full pipeline run:** After deleting the generated outputs, Snakemake successfully executed the complete workflow, finishing 5 of 5 steps.

**Forced partial rerun:** Running `snakemake --cores 1 --forcerun clean_samples` executed the cleaning, merging, and reporting steps without rerunning the database query.

**Upstream input modification:** A temporary change to the `notes` column of `messy_samples.csv` triggered the cleaning, merging, and reporting steps while leaving the database-query step unchanged.

The original input file was restored after testing.

## Output Files

- `results/cleaned_samples.csv` — cleaned Lab 3 sample data
- `results/feature_table.tsv` — patient feature table from Lab 4
- `results/combined_table.csv` — combined dataset
- `results/summary_report.txt` — final summary report

## Limitations

The source datasets do not share matching patient identifiers. As a result, the combined table is a vertically concatenated dataset rather than a patient-level join. Missing values for columns that are specific to only one dataset are expected.

## AI Assistance

OpenAI was used to help develop and troubleshoot the Snakemake workflow and supporting scripts.