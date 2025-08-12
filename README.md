# C++ Binary Search Tree Benchmarking

This project provides a framework for benchmarking the performance of three different types of binary search trees: a basic Binary Search Tree (BST), a Red-Black Tree (RB-Tree), and a Splay Tree.

The C++ source code implements the data structures and a main driver program to measure the time taken for insertion, search, and delete operations, as well as the final height of the trees after insertion. The project also includes a suite of scripts to automate the entire process of building the code, running the benchmarks, parsing the results, and generating plots.

## Project Structure

- `bst/`: Contains the source code for the Basic BST.
- `rb_tree/`: Contains the source code for the Red-Black Tree.
- `splay_tree/`: Contains the source code for the Splay Tree.
- `data/`: Contains the data files for insertion, search, and delete operations, organized into sets.
- `script/`: Contains the scripts for running the benchmarks, parsing results, and plotting charts.
- `bin/`: This directory is created by the Makefile and contains the compiled executables.
- `results/`: This directory is created by the scripts and contains the raw benchmark output, summary CSV files, and plots.
- `Makefile`: The build script for the project.

## Setup

To build the C++ programs, simply run the `make` command in the root of the project directory:

```bash
make
```

This will compile the source code for all three tree types and place the executables (`bst`, `rb_tree`, `splay_tree`) in the `bin/` directory.

## Usage

The project provides a fully automated pipeline for running the benchmarks and generating the results. To run the entire pipeline, use the following command:

```bash
make run
```

This command will:

1.  Compile the C++ programs (if they haven't been compiled already).
2.  Run the benchmarks for all tree types and data sets.
3.  Parse the raw benchmark output and generate summary CSV files in `results/`.
4.  Generate plots from the CSV files and save them in `results/charts/`.

### Makefile Targets

You can also run individual parts of the pipeline using specific `make` targets:

- `make all`: Compiles all the C++ programs. This is the default target.
- `make benchmarks`: Runs the benchmarks and generates the raw output files in `results/`.
- `make results`: Parses the raw benchmark output and creates the summary CSV files.
- `make plot`: Generates plots from the CSV files.
- `make clean`: Removes the `bin/` and `results/` directories, cleaning up all generated files.
