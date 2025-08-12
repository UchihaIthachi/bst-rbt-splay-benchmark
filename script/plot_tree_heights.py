import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV: columns = ["dataset", "BST", "Splay", "RBTree"]
df = pd.read_csv("../results/insert_times.csv")

# Plot
df.plot(x="dataset", kind="bar")
plt.title("Insertion Time Comparison")
plt.ylabel("Time (microseconds)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("../results/charts/insertion_times.png")
plt.show()
