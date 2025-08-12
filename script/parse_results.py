import os
import re

def parse_file(filepath):
    """Parses a result file and returns a dictionary of key-value pairs."""
    results = {}
    with open(filepath, 'r') as f:
        for line in f:
            match = re.match(r'([^,]+),(.+)', line)
            if match:
                key, value = match.groups()
                if 'time_ns' in key:
                    # Convert nanoseconds to microseconds for consistency in reporting
                    results['time_us'] = str(int(value.strip()) // 1000)
                else:
                    results[key] = value.strip()
    return results

def main():
    results_dir = 'results/insert'
    output_time_file = 'results/insert_times.csv'
    output_height_file = 'results/tree_heights.csv'

    runners_map = {
        'bst_runner': 'Basic BST',
        'splay_runner': 'Splay Tree',
        'rb_runner': 'RB-Tree'
    }
    
    datasets = []
    for set_num in [1, 2]:
        for data_num in [1, 2, 3]:
            datasets.append(f'set{set_num}/data_{data_num}')

    # --- Process data ---
    # data structure: { 'dataset_name': { 'tree_type': {'time_us': 123, 'height': 45} } }
    all_data = {}

    for dataset_name in datasets:
        all_data[dataset_name] = {}
        sanitized_dataset_name = dataset_name.replace('/', '_')
        for runner_id, runner_name in runners_map.items():
            result_filename = f'{runner_id}_{sanitized_dataset_name}.txt'
            result_filepath = os.path.join(results_dir, result_filename)
            
            if os.path.exists(result_filepath):
                parsed_data = parse_file(result_filepath)
                all_data[dataset_name][runner_name] = parsed_data
            else:
                print(f"Warning: Result file not found at {result_filepath}")
                all_data[dataset_name][runner_name] = {'time_us': 'N/A', 'height': 'N/A'}

    # --- Write CSV files ---
    header = ['Data set', 'Basic BST', 'Splay Tree', 'RB-Tree']
    
    # Write insert times
    with open(output_time_file, 'w') as f_time:
        f_time.write(','.join(header) + '\n')
        for dataset_name in datasets:
            row_data = [dataset_name]
            # Ensure order matches header
            for tree_name in header[1:]:
                time_val = all_data[dataset_name].get(tree_name, {}).get('time_us', 'N/A')
                row_data.append(time_val)
            f_time.write(','.join(row_data) + '\n')

    # Write tree heights
    with open(output_height_file, 'w') as f_height:
        f_height.write(','.join(header) + '\n')
        for dataset_name in datasets:
            row_data = [dataset_name]
            # Ensure order matches header
            for tree_name in header[1:]:
                height_val = all_data[dataset_name].get(tree_name, {}).get('height', 'N/A')
                row_data.append(height_val)
            f_height.write(','.join(row_data) + '\n')

    print(f"CSV files generated: {output_time_file} and {output_height_file}")

if __name__ == '__main__':
    main()
