import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_results(csv_file, y_label, title, output_filename):
    """Generates and saves a bar chart from a CSV file."""
    if not os.path.exists(csv_file):
        print(f"Warning: CSV file not found at {csv_file}. Skipping plot.")
        return

    df = pd.read_csv(csv_file)
    
    # Ensure 'Data set' is the index for plotting
    df.set_index('Data set', inplace=True)

    # Create the plot
    ax = df.plot(kind='bar', figsize=(12, 7), rot=45)
    
    # Set labels and title
    ax.set_ylabel(y_label)
    ax.set_xlabel("Data Set")
    ax.set_title(title)
    plt.tight_layout()
    
    # Save the chart
    charts_dir = 'results/charts'
    os.makedirs(charts_dir, exist_ok=True)
    plt.savefig(os.path.join(charts_dir, output_filename))
    print(f"Generated chart: {os.path.join(charts_dir, output_filename)}")
    plt.close()

def main():
    """Main function to generate all plots."""
    plot_results(
        csv_file='results/insert_times.csv',
        y_label='Time (microseconds)',
        title='Insertion Time Comparison',
        output_filename='insertion_times.png'
    )
    
    plot_results(
        csv_file='results/tree_heights.csv',
        y_label='Tree Height',
        title='Final Tree Height Comparison',
        output_filename='tree_heights.png'
    )

    plot_results(
        csv_file='results/search_times.csv',
        y_label='Time (microseconds)',
        title='Search Time Comparison',
        output_filename='search_times.png'
    )

    plot_results(
        csv_file='results/delete_times.csv',
        y_label='Time (microseconds)',
        title='Deletion Time Comparison',
        output_filename='delete_times.png'
    )

if __name__ == '__main__':
    main()
