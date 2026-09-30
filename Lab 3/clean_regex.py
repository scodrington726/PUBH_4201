import csv
import re
from datetime import datetime
from pathlib import Path

source_path = Path("/Users/summercodrington/Documents/PUBH_4201/data/messy_samples.csv")
out_path = Path("/Users/summercodrington/Documents/PUBH_4201/Lab 3/output/regex_cleaned.csv")


def clean_sample_id(value):
    digits = re.sub(r"\D", "", str(value).strip())
    if not digits:
        return ""
    return f"S{int(digits):04d}"


def clean_name(value):
    text = str(value).strip()
    if not text:
        return ""
    parts = text.replace("-", " ").split()
    cleaned = []
    for part in parts:
        if not part:
            continue
        part = re.sub(r"[^A-Za-z.]", "", part)
        if not part:
            continue
        if part.endswith(".") and len(part) == 2:
            cleaned.append(part.upper())
        else:
            cleaned.append(part[:1].upper() + part[1:].lower())
    return " ".join(cleaned)


def clean_dob(value):
    text = str(value).strip()
    if not text:
        return ""
    formats = [
        "%m/%d/%Y",
        "%m/%d/%y",
        "%Y-%m-%d",
        "%d-%b-%Y",
        "%d-%B-%Y",
        "%d.%m.%Y",
        "%d.%m.%y",
        "%m.%d.%Y",
        "%m.%d.%y",
        "%d-%b-%y",
        "%Y/%m/%d",
        "%m-%d-%Y",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(text, fmt).strftime("%m/%d/%Y")
        except ValueError:
            continue
    return text


def clean_sex(value):
    text = str(value).strip().lower()
    if text in {"", "u", "unknown"}:
        return "Unknown"
    if text in {"f", "female"}:
        return "Female"
    if text in {"m", "male"}:
        return "Male"
    return "Unknown"


def clean_site(value):
    text = str(value).strip().lower()
    if not text:
        return ""
    site_match = re.search(r"site[\s_\-]*([abc])", text)
    if site_match:
        return f"Site {site_match.group(1).upper()}"
    if text in {"a", "site a", "sitea"}:
        return "Site A"
    if text in {"b", "site b", "siteb"}:
        return "Site B"
    if text in {"c", "site c", "sitec"}:
        return "Site C"
    return ""


def clean_glucose(value, unit):
    text = str(value).strip().replace("*", "")
    unit_text = str(unit).strip().lower()
    if text.upper() == "N/A" or not text:
        return "", "mg/dL"
    try:
        numeric = float(text)
    except ValueError:
        return "", "mg/dL"

    if unit_text in {"mmol/l", "mmol/liter", "mmol", "mmol/l"}:
        numeric = numeric * 18.018
    return f"{numeric:.1f}", "mg/dL"


def clean_row(row):
    cleaned = {**row}
    cleaned["sample_id"] = clean_sample_id(row.get("sample_id", ""))
    cleaned["patient_name"] = clean_name(row.get("patient_name", ""))
    cleaned["dob"] = clean_dob(row.get("dob", ""))
    cleaned["sex"] = clean_sex(row.get("sex", ""))
    cleaned["enrollment_site"] = clean_site(row.get("enrollment_site", ""))
    value, unit = clean_glucose(row.get("glucose_value", ""), row.get("glucose_unit", ""))
    cleaned["glucose_value"] = value
    cleaned["glucose_unit"] = unit
    cleaned["notes"] = str(row.get("notes", "")).strip()
    return cleaned


with source_path.open("r", newline="") as infile:
    reader = csv.DictReader(infile)
    rows = [clean_row(row) for row in reader]

fieldnames = [
    "sample_id",
    "patient_name",
    "dob",
    "sex",
    "enrollment_site",
    "glucose_value",
    "glucose_unit",
    "notes",
]

with source_path.open("w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

with out_path.open("w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Cleaned {len(rows)} rows and saved to {source_path} and {out_path}")
