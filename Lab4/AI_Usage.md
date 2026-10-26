# AI Usage — PUBH 4201 Lab 4

## AI Tool Used

OpenAI was used to assist with completing Lab 4: Database-Driven Feature Table.

## How AI Was Used

I used ChatGPT to help with:

- Troubleshooting my Python and Mamba environment in VS Code.
- Understanding the database structure and identifying relationships between tables.
- Developing Python scripts to execute SQL queries and construct a patient-level feature 
- Checking missing values, patient counts, and duplicate records.
- Creating the data dictionary and documenting the workflow.

## How I Verified the AI-Generated Work

I ran the provided Python scripts and SQL queries against the actual `cohort.db` database.

**1. Database verification**

I inspected the database and confirmed that it contained four tables: patients, samples, genes, and mutations.

**2. SQL row-count verification**

The mutation-count query returned 700 patient–gene combinations.

The tissue source site and tumor stage query returned 142 groups.

I checked that these outputs represented the expected grouping levels rather than assuming that every query should return 566 rows.

**3. Feature table verification**

I confirmed that the patient count remained 566 before and after combining the data. The final feature table contained 566 unique patient IDs and no duplicates.

**4. Manual mutation verification**

I independently checked patient `TCGA-05-4382` for EGFR mutations.

The original database returned two non-Silent mutations, with mutation IDs 2635 and 2636. Both were classified as `Missense_Mutation`.

The feature table also showed an EGFR mutation count of 2 for this patient.

The verification script confirmed that the counts matched.

**5. Missing-data verification**

I checked the missing values in the final feature table:

- Sex: 52 missing
- Age at diagnosis: 71 missing
- Tumor stage: 54 missing

I preserved missing clinical values and used zeros for gene counts when no qualifying mutation was recorded.

## Reflection

AI helped me troubleshoot technical errors and understand how SQL and Python can be combined to work with relational databases.

The code, outputs, and explanations were reviewed during the lab process.
