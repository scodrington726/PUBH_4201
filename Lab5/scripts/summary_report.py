
import pandas as pd
from pathlib import Path

# Read the combined dataset
df = pd.read_csv("results/combined_table.csv")

# Count records by source
source_counts = df["data_source"].value_counts()

# Count missing values in each column
missing_values = df.isna().sum()

# Create summary report
report = [
    "LAB 5: SCALABLE ANALYSIS WORKFLOW",
    "================================",
    "",
    f"Total records: {len(df)}",
    "",
    "Records by dataset:",
    source_counts.to_string(),
    "",
    "Missing values by column:",
    missing_values.to_string(),
    "",
    "Data integration note:",
    "Lab 3 and Lab 4 have no matching patient IDs.",
    "The datasets were stacked rather than joined by patient.",
    "Therefore, rows do not represent matched patient records."
]

# Save report
output_path = Path("results/summary_report.txt")
output_path.write_text("\n".join(report))

print("Summary report saved to", output_path)
