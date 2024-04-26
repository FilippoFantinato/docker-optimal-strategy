#!/bin/bash
#SBATCH --job-name="ASAP Benchmarks co-safety third"
#SBATCH --error=co-safety-third.err
#SBATCH --output=co-safety-third.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-co-safety-third-benchmark
