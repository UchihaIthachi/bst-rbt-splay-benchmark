import os
import re
import pandas as pd

def parse_file(filepath):
    """Parses a result file and returns a dictionary of key-value pairs."""
    results = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                match = re.match(r'([^,]+),(.+)', line)
                if match:
                    key, value = match.groups()
                    results[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Warning: File not found {filepath}")
        return None
    return results

def process_operation(op_name, executables, data_sets, results_dir):
    """Processes results for a given operation (insert, search, delete)."""
    data = {"Data set": [d.replace(".txt", "") for d in data_sets]}
    
    for exe, tree_name in executables.items():
        times = []
        heights = [] if op_name == "insert" else None
        for data_file in data_sets:
            data_set_name = os.path.splitext(os.path.basename(data_file))[0]
            set_name = os.path.basename(os.path.dirname(data_file))
            
            result_filename = f"{tree_name}_{set_name}_{data_set_name}.txt"
            result_filepath = os.path.join(results_dir, op_name, result_filename)
            
            parsed_data = parse_file(result_filepath)
            
            if parsed_data:
                if op_name == "insert":
                    times.append(parsed_data.get('time_us', 'N/A'))
                    heights.append(parsed_data.get('height', 'N/A'))
                else:
                    key_name = f'search_time_us' if op_name == 'search' else f'delete_time_us'
                    times.append(parsed_data.get(key_name, 'N/A'))
            else:
                times.append('N/A')
                if heights is not None:
                    heights.append('N/A')

        data[f"{tree_name}_time"] = times
        if heights is not None:
            data[f"{tree_name}_height"] = heights

    # Create pivot tables
    time_df = pd.DataFrame({'Data set': data['Data set']})
    height_df = None
    if op_name == "insert":
        height_df = pd.DataFrame({'Data set': data['Data set']})

    for exe, tree_name in executables.items():
        time_df[tree_name] = data[f"{tree_name}_time"]
        if height_df is not None:
            height_df[tree_name] = data[f"{tree_name}_height"]

    return time_df, height_df


def main():
    results_dir = 'results'
    
    executables = {
        "bin/bst": "BST",
        "bin/rb_tree": "RBTree",
        "bin/splay_tree": "SplayTree"
    }

    data_sets = [f"set{s}/data_{d}.txt" for s in [1, 2] for d in [1, 2, 3]]

    # Process Insertion
    insert_time_df, height_df = process_operation("insert", executables, data_sets, results_dir)
    
    # Process Search
    search_time_df, _ = process_operation("search", executables, data_sets, results_dir)

    # Process Deletion
    delete_time_df, _ = process_operation("delete", executables, data_sets, results_dir)
    
    # Save to CSV
    header_order = ['Data set', 'BST', 'SplayTree', 'RBTree']
    
    if insert_time_df is not None:
        insert_time_df.rename(columns={'BST': 'Basic BST', 'SplayTree': 'Splay Tree', 'RBTree': 'RB-Tree'}, inplace=True)
        insert_time_df.to_csv(os.path.join(results_dir, 'insert_times.csv'), index=False)
        print(f"Generated {os.path.join(results_dir, 'insert_times.csv')}")
    
    if height_df is not None:
        height_df.rename(columns={'BST': 'Basic BST', 'SplayTree': 'Splay Tree', 'RBTree': 'RB-Tree'}, inplace=True)
        height_df.to_csv(os.path.join(results_dir, 'tree_heights.csv'), index=False)
        print(f"Generated {os.path.join(results_dir, 'tree_heights.csv')}")

    if search_time_df is not None:
        search_time_df.rename(columns={'BST': 'Basic BST', 'SplayTree': 'Splay Tree', 'RBTree': 'RB-Tree'}, inplace=True)
        search_time_df.to_csv(os.path.join(results_dir, 'search_times.csv'), index=False)
        print(f"Generated {os.path.join(results_dir, 'search_times.csv')}")
    
    if delete_time_df is not None:
        delete_time_df.rename(columns={'BST': 'Basic BST', 'SplayTree': 'Splay Tree', 'RBTree': 'RB-Tree'}, inplace=True)
        delete_time_df.to_csv(os.path.join(results_dir, 'delete_times.csv'), index=False)
        print(f"Generated {os.path.join(results_dir, 'delete_times.csv')}")


if __name__ == '__main__':
    main()
