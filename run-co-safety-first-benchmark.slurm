#!/bin/bash
#SBATCH --job-name="ASAP Benchmarks co-safety first"
#SBATCH --error=co-safety-first.err
#SBATCH --output=co-safety-first.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-co-safety-first-benchmark
