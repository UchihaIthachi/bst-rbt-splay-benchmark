# Makefile for Tree Benchmarking

CXX = g++
CXXFLAGS = -std=c++11 -O2 -Wall

# Executables
RUNNERS = bst_runner rb_runner splay_runner

# Phony targets
.PHONY: all clean

all: $(RUNNERS)

bst_runner: bst_main.cpp bst/BST.h
	$(CXX) $(CXXFLAGS) -o $@ $<

rb_runner: rb_main.cpp rb_tree/RBTree.h
	$(CXX) $(CXXFLAGS) -o $@ $<

splay_runner: splay_main.cpp splay_tree/SplayTree.h
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(RUNNERS)
