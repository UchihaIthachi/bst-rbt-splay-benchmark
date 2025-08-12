#include "RBTree.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <string>
#include <chrono>
#include <algorithm>

// Function to read integers from a file into a vector
void read_data(const std::string& filename, std::vector<long long>& data) {
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        long long value;
        if (ss >> value) {
            data.push_back(value);
        }
    }
}

int height(RBTree::Node* r) {
    if (!r) return -1;
    return 1 + std::max(height(r->left), height(r->right));
}

int main(int argc, char* argv[]) {
    if (argc < 2 || argc > 3) {
        std::cerr << "Usage: " << argv[0] << " <insert_file> [<op_file>]" << std::endl;
        return 1;
    }

    std::string insert_file = argv[1];
    std::vector<long long> insert_values;
    read_data(insert_file, insert_values);

    // Part (a): Insertion measurement
    if (argc == 2) {
        RBTree tree;
        auto t0 = std::chrono::steady_clock::now();
        for (long long x : insert_values) {
            tree.put(x, x);
        }
        auto t1 = std::chrono::steady_clock::now();
        auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
        int final_height = height(tree.getRoot());

        std::cout << "time_us," << us << std::endl;
        std::cout << "height," << final_height << std::endl;
    } 
    // Parts (b) and (c): Search or Delete measurement
    else if (argc == 3) {
        // First, build the tree with the insert data
        RBTree tree;
        for (long long x : insert_values) {
            tree.put(x, x);
        }

        std::string op_file = argv[2];
        std::vector<long long> op_values;
        read_data(op_file, op_values);

        // Discern operation based on filename
        if (std::string(op_file).find("search") != std::string::npos) {
            auto t0 = std::chrono::steady_clock::now();
            for (long long x : op_values) {
                tree.contains(x);
            }
            auto t1 = std::chrono::steady_clock::now();
            auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
            std::cout << "search_time_us," << us << std::endl;
        } else if (std::string(op_file).find("delete") != std::string::npos) {
            auto t0 = std::chrono::steady_clock::now();
            for (long long x : op_values) {
                tree.del(x);
            }
            auto t1 = std::chrono::steady_clock::now();
            auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
            std::cout << "delete_time_us," << us << std::endl;
        } else {
            std::cerr << "Operation file must contain 'search' or 'delete' in its path." << std::endl;
            return 1;
        }
    }

    return 0;
}
