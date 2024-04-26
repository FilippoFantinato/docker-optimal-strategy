#!/bin/bash
#SBATCH --job-name="All ASAP Benchmarks finally"
#SBATCH --error=driver-finally.err
#SBATCH --output=driver-finally.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-driver-finally-benchmark
