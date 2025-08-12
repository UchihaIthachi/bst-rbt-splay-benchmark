#!/bin/bash

# This script runs the insertion benchmarks for all tree types and data sets.

RESULTS_DIR="results/insert"
DATA_DIR="data/insert"

# Ensure the results directory exists
mkdir -p "$RESULTS_DIR"

TREE_RUNNERS=("bst_runner" "rb_runner" "splay_runner")
SETS=("set1" "set2")

for runner in "${TREE_RUNNERS[@]}"; do
    tree_type=$(echo "$runner" | cut -d'_' -f1)
    for set_name in "${SETS[@]}"; do
        for i in {1..3}; do
            data_file="${DATA_DIR}/${set_name}/data_${i}.txt"
            output_file="${RESULTS_DIR}/${tree_type}_runner_${set_name}_data_${i}.txt"
            echo "Running $runner with $data_file..."
            ./"$runner" "$data_file" > "$output_file"
        done
    done
done

echo "All insertion benchmarks complete."
