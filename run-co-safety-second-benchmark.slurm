#!/bin/bash
#SBATCH --job-name="ASAP Benchmarks co-safety second"
#SBATCH --error=co-safety-second.err
#SBATCH --output=co-safety-second.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-co-safety-second-benchmark
