# AI Usage

## Tool Used
ChatGPT (OpenAI)

## How I Used AI

I used ChatGPT while completing this lab to help me understand terminal commands, Conda/Mamba environments, Git repository setup, and dependency errors.

### Conda environment
I asked ChatGPT what the `prefix:` line in `environment.yml` meant and why the instructions required me to delete it. ChatGPT explained that the prefix contains the environment path specific to my computer and would make the file less portable. I verified this by reviewing the exported `environment.yml` and then removed the prefix line.

### Dependency conflict
During the Week 2 exercise, I intentionally added `numpy=1.19` alongside `pandas=2.2` and asked ChatGPT what the resulting Mamba error meant before asking how to fix it. ChatGPT explained that pandas 2.2 requires a newer version of NumPy and that Mamba's dependency resolver was preventing incompatible package versions from being installed.

I removed the incompatible NumPy pin and recreated the environment. I verified the fix by successfully running:

mamba env create -f environment.yml

and then:

python src/analyze.py

The analysis produced the same output as before the environment was deleted.

### Git setup
I also used ChatGPT to help diagnose why `git status` was showing files from my entire home directory. I checked the repository root using:

git rev-parse --show-toplevel

This showed that Git had been initialized in my home directory instead of my PUBH_4201 project folder. After correcting the repository location, I verified that `git status` only displayed files belonging to the project.

## What I Changed or Rejected

I did not blindly copy every suggested command. I checked my current directory and file locations before running commands, verified the contents of `environment.yml`, and tested the recreated environment by running the analysis script and comparing the output.