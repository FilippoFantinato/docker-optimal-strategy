#!/bin/bash
#SBATCH --job-name="ASAP Benchmarks both second"
#SBATCH --error=both-second.err
#SBATCH --output=both-second.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-both-second-benchmark
