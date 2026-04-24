# FASTA Sequence Analyzer

## Purpose
The goal of this project is to learn the basics of Python through 
a concrete bioinformatics use case: quality control of 16S rRNA sequences.

## Pipeline Structure
The project is divided into independent modules, each handling one step:

1. **Load data** — parse a FASTA file and extract sequence information
2. **Global statistics** — count, mean length, min/max, std, N50
3. **Sequence composition** — GC content, N percentage, Shannon entropy
4. **Quality filtering** — flag and reject sequences based on QC thresholds
5. **Summary** — display results in the terminal

A `main.py` script connects all modules and runs the entire pipeline.

## Skills Practiced
- Functions and modules
- Loops and list comprehensions
- File reading
- Dictionaries and lists of dictionaries

## Requirements
- Python 3.11+
- Biopython (`pip install biopython`)

## Usage
```bash
