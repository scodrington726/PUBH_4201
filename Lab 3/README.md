## Lab 3: Parsing Messy Health Data

### Overview
This lab compares regex-based and AI-assisted approaches to cleaning a synthetic clinical dataset containing 60 records with inconsistent formatting.

### Dataset
The input dataset is `data/messy_samples.csv`.

### Regex Cleaning
The Python script standardizes sample IDs, dates, sex values, enrollment site names, glucose measurements, and inconsistent entries.

To run the script from the PUBH_4201 repository root:

```bash
python "Lab 3/clean_regex.py"
```

The script uses Python and pandas.

### Outputs
- `Lab 3/output/regex_cleaned.csv` — Regex-based cleaning output.
- `Lab 3/output/ai_cleaned.csv` — AI-assisted cleaning output.
- `Lab 3/AI_USAGE.md` — Documents the AI prompts used.
- `Lab 3/comparison.md` — Compares both approaches and discusses specific failure cases.

### Reproducibility
The original dataset is retained separately from the cleaned outputs. Both methods use the same input data to allow direct comparison.
