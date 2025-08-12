import os

def count_data(filepath):
    """Counts the numbers in a data file."""
    with open(filepath, 'r') as f:
        content = f.read()
        # Handle potential empty strings from trailing commas
        numbers = [p for p in content.split(',') if p.strip()]
        return len(numbers)

def main():
    data_file = 'data/insert/set1/data_1.txt'
    if os.path.exists(data_file):
        count = count_data(data_file)
        print(f"Number of items in {data_file}: {count}")
    else:
        print(f"Data file not found: {data_file}")

if __name__ == '__main__':
    main()
