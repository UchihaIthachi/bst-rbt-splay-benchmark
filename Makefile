CXX = g++
CXXFLAGS = -std=c++11 -Wall -O2

# Phony targets to avoid conflicts with filenames
.PHONY: all clean benchmarks results plot run

all: bin/bst bin/rb_tree bin/splay_tree

bin/bst: bst/bst_main.cpp bst/BST.h
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) -o $@ $<

bin/rb_tree: rb_tree/rb_main.cpp rb_tree/RBTree.h
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) -o $@ $<

bin/splay_tree: splay_tree/splay_main.cpp splay_tree/SplayTree.h
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) -o $@ $<

benchmarks: all
	@echo "Running benchmarks..."
	@script/run_benchmarks.sh

results: benchmarks
	@echo "Parsing results..."
	@python3 script/parse_results.py

plot: results
	@echo "Generating plots..."
	@python3 script/plot_results.py

run: all benchmarks results plot
	@echo "Full pipeline complete."

clean:
	@echo "Cleaning up..."
	@rm -rf bin results
