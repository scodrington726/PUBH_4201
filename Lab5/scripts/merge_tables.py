
import pandas as pd

# Load the outputs from Labs 3 and 4
samples = pd.read_csv(
    "results/cleaned_samples.csv",
    dtype={"sample_id": str}
)

features = pd.read_csv("results/feature_table.tsv", sep="\t")

# Identify the source of each record
samples["data_source"] = "Lab 3"
features["data_source"] = "Lab 4"

# Combine both datasets while preserving all rows
combined = pd.concat(
    [samples, features],
    ignore_index=True,
    sort=False
)

# Save the combined table
combined.to_csv("results/combined_table.csv", index=False)

print("Lab 3 rows:", len(samples))
print("Lab 4 rows:", len(features))
print("Combined rows:", len(combined))
print("Saved results/combined_table.csv")
