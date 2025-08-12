#!/bin/bash

# This script runs the benchmarks for all tree types and data sets.

# --- Setup ---
RESULTS_DIR="results"
DATA_DIR="data"
BIN_DIR="bin"

# Ensure the results directory exists
mkdir -p "$RESULTS_DIR/insert"
mkdir -p "$RESULTS_DIR/search"
mkdir -p "$RESULTS_DIR/delete"

# Clean previous results
rm -f "$RESULTS_DIR/insert"/*
rm -f "$RESULTS_DIR/search"/*
rm -f "$RESULTS_DIR/delete"/*

declare -A executables
executables["$BIN_DIR/bst"]="BST"
executables["$BIN_DIR/rb_tree"]="RBTree"
executables["$BIN_DIR/splay_tree"]="SplayTree"

data_sets=("set1/data_1.txt" "set1/data_2.txt" "set1/data_3.txt" "set2/data_1.txt" "set2/data_2.txt" "set2/data_3.txt")

# --- Part (a): Insertion ---
echo "Running insertion benchmarks..."
for exe in "${!executables[@]}"; do
    tree_type=${executables[$exe]}
    for data_file in "${data_sets[@]}"; do
        data_set_name=$(basename "${data_file}" .txt)
        set_name=$(basename $(dirname ${data_file}))
        output_file="${RESULTS_DIR}/insert/${tree_type}_${set_name}_${data_set_name}.txt"
        echo "  Inserting ${data_file} into ${tree_type}..."
        ./"$exe" "${DATA_DIR}/insert/${data_file}" > "$output_file"
    done
done

# --- Part (b): Searching ---
echo "Running search benchmarks..."
for exe in "${!executables[@]}"; do
    tree_type=${executables[$exe]}
    for data_file in "${data_sets[@]}"; do
        data_set_name=$(basename "${data_file}" .txt)
        set_name=$(basename $(dirname ${data_file}))
        output_file="${RESULTS_DIR}/search/${tree_type}_${set_name}_${data_set_name}.txt"
        echo "  Searching ${data_file} in ${tree_type}..."
        search_file="${DATA_DIR}/search/${data_file}"
        insert_file="${DATA_DIR}/insert/${data_file}"
        
        ./"$exe" "${insert_file}" "${search_file}" > "$output_file"
    done
done

# --- Part (c): Deletion ---
echo "Running deletion benchmarks..."
for exe in "${!executables[@]}"; do
    tree_type=${executables[$exe]}
    for data_file in "${data_sets[@]}"; do
        data_set_name=$(basename "${data_file}" .txt)
        set_name=$(basename $(dirname ${data_file}))
        output_file="${RESULTS_DIR}/delete/${tree_type}_${set_name}_${data_set_name}.txt"
        echo "  Deleting ${data_file} from ${tree_type}..."
        delete_file="${DATA_DIR}/delete/${data_file}"
        insert_file="${DATA_DIR}/insert/${data_file}"
        
        ./"$exe" "${insert_file}" "${delete_file}" > "$output_file"
    done
done

echo "Benchmarking complete. Results are in the 'results' directory."
