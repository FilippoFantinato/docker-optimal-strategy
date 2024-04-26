#!/bin/bash
#SBATCH --job-name="ASAP Benchmarks both first"
#SBATCH --error=both-first.err
#SBATCH --output=both-first.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-both-first-benchmark
