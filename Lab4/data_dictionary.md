# Data Dictionary — Lab 4

**Dataset:** TCGA Lung Adenocarcinoma PanCancer Atlas

**Output file:** `feature_table.tsv`

**Grain:** One row per patient (566 total patients)

| Column | Meaning | Units | Source |
|---|---|---|---|
| `patient_id` | Unique patient identifier | None | patients |
| `sex` | Patient's recorded sex | Categorical | patients |
| `age_at_diagnosis` | Patient's age at diagnosis | Years | patients |
| `stage` | Tumor stage at diagnosis | Categorical | patients |
| `tissue_source_site` | Institution or site associated with the tumor sample | Categorical | samples |
| `tmb_nonsynonymous` | Tumor mutation burden based on nonsynonymous mutations | Mutations per megabase (verify source definition) | samples |
| `mut_TP53` | Number of recorded non-Silent TP53 mutations | Mutation count | mutations, samples |
| `mut_KRAS` | Number of recorded non-Silent KRAS mutations | Mutation count | mutations, samples |
| `mut_EGFR` | Number of recorded non-Silent EGFR mutations | Mutation count | mutations, samples |
| `mut_STK11` | Number of recorded non-Silent STK11 mutations | Mutation count | mutations, samples |
| `mut_KEAP1` | Number of recorded non-Silent KEAP1 mutations | Mutation count | mutations, samples |

## Missing Data Handling

Clinical missing values were preserved as missing rather than replaced with estimated values.

- Sex: 52 missing
- Age at diagnosis: 71 missing
- Tumor stage: 54 missing
- Tissue source site: 0 missing
- Tumor mutation burden: 0 missing

Mutation counts were assigned a value of zero when no qualifying mutation was recorded for a particular patient and gene. This is different from missing clinical information.

A total of 109 patients had zero recorded qualifying mutations across all five selected genes.

## Validation

The starting patient table contained 566 patients, and the final feature table contained 566 rows representing 566 unique patients.

No duplicate patient IDs were found.

A manual database verification of patient `TCGA-05-4382` identified two non-Silent EGFR mutations (`2635` and `2636`), consistent with the final feature table.
