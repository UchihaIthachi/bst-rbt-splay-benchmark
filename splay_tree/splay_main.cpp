#include "SplayTree.h"
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
    std::getline(file, line);
    std::stringstream ss(line);
    std::string value;
    while (std::getline(ss, value, ',')) {
        if (!value.empty()) {
            try {
                data.push_back(std::stoll(value));
            } catch (const std::invalid_argument& e) {
                // Ignore invalid numbers
            } catch (const std::out_of_range& e) {
                // Ignore numbers out of range
            }
        }
    }
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
        SplayTree tree;
        auto t0 = std::chrono::steady_clock::now();
        for (long long x : insert_values) {
            tree.put(x, x);
        }
        auto t1 = std::chrono::steady_clock::now();
        auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(t1 - t0).count();
        size_t final_height = tree.height();

        std::cout << "time_ns," << ns << std::endl;
        std::cout << "height," << final_height << std::endl;
        std::cout << "dummy,0" << std::endl; // Keep dummy for consistent output format
    } 
    // Parts (b) and (c): Search or Delete measurement
    else if (argc == 3) {
        // First, build the tree with the insert data
        SplayTree tree;
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
            auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(t1 - t0).count();
            std::cout << "search_time_ns," << ns << std::endl;
        } else if (std::string(op_file).find("delete") != std::string::npos) {
            auto t0 = std::chrono::steady_clock::now();
            for (long long x : op_values) {
                tree.del(x);
            }
            auto t1 = std::chrono::steady_clock::now();
            auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(t1 - t0).count();
            std::cout << "delete_time_ns," << ns << std::endl;
        } else {
            std::cerr << "Operation file must contain 'search' or 'delete' in its path." << std::endl;
            return 1;
        }
    }

    return 0;
}
