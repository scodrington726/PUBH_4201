# Regex vs AI Assisted Cleaning Comparsion
## 1. Where did they agree/disagree?
### Both approaches successfully retained all 60 records and standardized the sample IDs, patient names, sex values, and glucose units consistently. Both also preserved missing glucose measurements rather than inventing values. However, differences appeared in the handling of dates, enrollment sites, and glucose conversions. Date formatting: The regex method produced dates in MM/DD/YYYY format, while the AI-assisted method used YYYY-MM-DD. Beyond this formatting difference, eight records contained substantive date disagreements. Enrollment sites: Some records had missing enrollment sites in the regex output, even though the original values were present as SITE-A. The AI-assisted method successfully standardized these entries to Site A.
## Which caught edge cases the other missed?
### The AI-assisted approach handled certain formatting variations that the regex implementation missed. For example, samples S0002, S0005, and S0009 contained the enrollment site SITE-A. The regex output left these fields blank, whereas AI successfully standardized them to Site A. The AI-assisted method also interpreted two-digit years differently. In sample S0021, the original DOB 02.26.64 became 02/26/2064 through regex and 1964-02-26 through AI. The regex method was useful for applying consistent, predefined rules. However, it required those rules to account for every formatting variation, and unexpected inputs exposed limitations in the implementation. Neither approach completely eliminated ambiguity, especially when interpreting dates without additional formatting context.
## 3. which was faster to get right?
### The AI was definitely faster, the Regex took more time to troubleshoot through.
# Task 4
## Failure 1: Incorrect Interpretation of DOB
### Original: 11.24.53
### Regex output: 11/24/2053
### AI output: 1953-11-24
### The regex method incorrectly interpreted the two-digit year 53 as 2053 rather than 1953. This occurred because the date-parsing function did not correctly account for the intended century when handling two-digit years. The AI-assisted approach produced a more plausible interpretation for this dataset. This example demonstrates how automated date parsing can produce technically valid but incorrect dates when the century is not explicitly defined.
### Failure 2: Missing Enrollment Site (S0002)
## Original enrollment site: SITE-A
## Regex output: Blank
## AI output: Site A
## The regex method failed to recognize the enrollment site because its cleaning rules did not properly account for the hyphenated, uppercase variation SITE-A. As a result, the original information was lost, even though it was present in the raw dataset. The AI-assisted method successfully interpreted the abbreviation and standardized it to Site A. This demonstrates how overly restrictive regex patterns can fail when they encounter unexpected formatting variations.