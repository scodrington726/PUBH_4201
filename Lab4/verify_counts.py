
import sqlite3
import pandas as pd

conn = sqlite3.connect("cohort.db")

patient_id = "TCGA-05-4382"
gene = "EGFR"

query = """
SELECT
    m.mutation_id,
    m.gene_symbol,
    m.variant_classification
FROM mutations AS m
JOIN samples AS s
    ON m.sample_id = s.sample_id
WHERE s.patient_id = ?
AND m.gene_symbol = ?
AND m.variant_classification != 'Silent'
"""

records = pd.read_sql_query(
    query,
    conn,
    params=(patient_id, gene)
)

features = pd.read_csv("feature_table.tsv", sep="\t")
stored_count = features.loc[
    features["patient_id"] == patient_id,
    "mut_EGFR"
].iloc[0]

print("Patient:", patient_id)
print("Gene:", gene)
print("\nIndividual qualifying mutations:")
print(records.to_string(index=False))

print("\nCount from database:", len(records))
print("Count in feature table:", stored_count)

assert len(records) == stored_count
print("Verification passed!")

conn.close()
