
# Task 1: Database Schema

The database contains four tables: patients, samples, genes, and mutations.

## Patients
- Grain: One row per patient.
- Rows: 566
- Columns: patient_id, sex, age_at_diagnosis, stage, vital_status, followup_months.
- Primary identifier: patient_id.

## Samples
- Grain: One row per tumor sample.
- Rows: 566
- Columns: sample_id, patient_id, tissue_source_site, tmb_nonsynonymous, aneuploidy_score, msi_mantis_score.
- Foreign key: patient_id references patients.patient_id.

## Genes
- Grain: One row per gene.
- Rows: 17,756
- Columns: gene_symbol, entrez_gene_id, chromosome.
- Primary identifier: gene_symbol.

## Mutations
- Grain: One row per recorded somatic mutation in a sample.
- Rows: 200,789
- Columns: mutation_id, sample_id, gene_symbol, variant_classification, variant_type, protein_change, chromosome, start_pos, end_pos, t_ref_count, t_alt_count.
- Foreign keys:
  - sample_id references samples.sample_id.
  - gene_symbol references genes.gene_symbol.

## Relationships
Patients are linked to samples through patient_id.
Samples are linked to mutations through sample_id.
Genes are linked to mutations through gene_symbol.
