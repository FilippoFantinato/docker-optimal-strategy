#!/bin/bash
#SBATCH --job-name="ASAP Benchmarks various formulas"
#SBATCH --error=various-formulas.err
#SBATCH --output=various-formulas.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-various-formulas
