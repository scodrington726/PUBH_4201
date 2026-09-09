# PUBH 4201 Reproducible Environment Project

This project demonstrates how to create and reproduce a Python analysis environment using Conda/Mamba. The project includes a Python analysis script, example patient data, and an `environment.yml` file that allows another user to recreate the computational environment.

## Project Structure

- `src/` - Includes the Python analysis script
- `data/` - Contains the project data
- `environment.yml` - Specifies the Conda environment and required packages
- `AI_USAGE.md` - Documents how AI was used during the project
- `.gitignore` - Specifies files that should not be tracked by Git

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/scodrington726/PUBH_4201.git
```

### 2. Enter the project directory

```bash
cd PUBH_4201
```

### 3. Create the environment

Using Mamba:

```bash
mamba env create -f environment.yml
```

### 4. Activate the environment

```bash
conda activate repro-demo
```

## Run the Analysis

Run the Python analysis script with:

```bash
python src/analyze.py
```

The script should produce descriptive statistics (mean, median, mode, etc) for the example patient age data.

## Reproducibility

The environment was tested by deleting the existing Conda environment and recreating it entirely from `environment.yml`. After recreating and activating the environment, the analysis script was run again and produced the same output.