#!/bin/bash
#SBATCH --job-name="ASAP Benchmarks both third"
#SBATCH --error=both-third.err
#SBATCH --output=both-third.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-both-third-benchmark
