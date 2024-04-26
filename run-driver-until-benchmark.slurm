#!/bin/bash
#SBATCH --job-name="ASAP Benchmarks driver until"
#SBATCH --error=driver-until.err
#SBATCH --output=driver-until.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
./run-driver-until-benchmark
