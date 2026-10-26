
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("cohort.db")

# Get patient information and sample measurements
patient_query = """
SELECT
    p.patient_id,
    p.sex,
    p.age_at_diagnosis,
    p.stage,
    s.tissue_source_site,
    s.tmb_nonsynonymous
FROM patients AS p
LEFT JOIN samples AS s
    ON p.patient_id = s.patient_id
"""

patients = pd.read_sql_query(patient_query, conn)

print("Patients after joining samples:", len(patients))

# Count qualifying mutations for each patient and gene
mutation_query = """
SELECT
    s.patient_id,
    m.gene_symbol,
    COUNT(*) AS mutation_count
FROM mutations AS m
JOIN samples AS s
    ON m.sample_id = s.sample_id
WHERE m.gene_symbol IN (
    'TP53', 'KRAS', 'EGFR', 'STK11', 'KEAP1'
)
AND m.variant_classification != 'Silent'
GROUP BY s.patient_id, m.gene_symbol
"""

mutations = pd.read_sql_query(mutation_query, conn)
conn.close()


wide_mutations = mutations.pivot(
    index="patient_id",
    columns="gene_symbol",
    values="mutation_count"
)


genes = ["TP53", "KRAS", "EGFR", "STK11", "KEAP1"]
wide_mutations = wide_mutations.reindex(columns=genes)


wide_mutations = wide_mutations.fillna(0).astype(int)
wide_mutations = wide_mutations.add_prefix("mut_")


features = patients.merge(
    wide_mutations,
    on="patient_id",
    how="left",
    validate="one_to_one"
)

gene_columns = [f"mut_{gene}" for gene in genes]
features[gene_columns] = (
    features[gene_columns].fillna(0).astype(int)
)

print("Final patient count:", len(features))
print("Unique patients:", features["patient_id"].nunique())


assert len(features) == 566
assert features["patient_id"].is_unique


features.to_csv(
    "feature_table.tsv",
    sep="\t",
    index=False
)

print("Saved feature_table.tsv")
print(features.head())

# Task 4: Check missing data

print("\nMissing values by column:")
print(features.isna().sum())

print("\nPatients with no mutations in the five genes:")
gene_columns = [
    "mut_TP53", "mut_KRAS", "mut_EGFR",
    "mut_STK11", "mut_KEAP1"
]

no_mutations = (features[gene_columns].sum(axis=1) == 0)
print(no_mutations.sum())


print("\nDuplicate patient IDs:")
print(features["patient_id"].duplicated().sum())
