#!/bin/bash
#SBATCH --job-name="All ASAP Benchmarks finally"
#SBATCH --error=all_benchmarks_finally.err
#SBATCH --output=all_benchmarks_finally.out
#SBATCH --partition=allgroups
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00
# ./run-both-first-benchmark
# ./run-both-second-benchmark
# ./run-both-third-benchmark
# ./run-co-safety-first-benchmark
# ./run-co-safety-second-benchmark
# ./run-co-safety-third-benchmark
./run-driver-finally-benchmark
# ./run-driver-until-benchmark
