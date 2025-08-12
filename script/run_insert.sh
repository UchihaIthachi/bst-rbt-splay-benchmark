#!/bin/bash

# Create a directory for raw insertion results
mkdir -p results/insert

# Define the tree executables
runners=("bst_runner" "rb_runner" "splay_runner")

# Define the datasets
sets=("set1" "set2")
files=("data_1" "data_2" "data_3")

# Loop through each runner and dataset
for runner in "${runners[@]}"; do
    for set in "${sets[@]}"; do
        for file in "${files[@]}"; do
            input_file="data/insert/${set}/${file}.txt"
            output_file="results/insert/${runner}_${set}_${file}.txt"
            echo "Running ${runner} on ${input_file}..."
            ./${runner} ${input_file} > ${output_file}
        done
    done
done

echo "All insertion experiments complete."
