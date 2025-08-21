import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (also available on GitHub: https://github.com/mwaskom/seaborn-data/blob/master/tips.csv)
data = sns.load_dataset("tips")

# Create a Strip Plot
sns.stripplot(
    data=data,          # DataFrame containing the data
    x="day",            # Categorical axis (grouping) — here: days of the week
    y="total_bill",     # Numeric axis — here: total bill amounts
    hue="sex",          # Color dots by gender (optional)
    dodge=True,         # Separates hue values for better readability
    jitter=0.25,        # Adds random noise to prevent overlapping (0 to 1 or True/False)
    palette="Set1",     # Set the color palette (e.g., 'Set1', 'husl', 'muted', etc.)
    size=5,             # Size of the dots
    marker="o",         # Shape of the dots (e.g., 'o', 's', 'D', '^')
    linewidth=0.5,      # Border thickness around dots
    edgecolor="gray",   # Color of the dot edges
    alpha=0.7           # Transparency of dots (0 to 1)
)

# Add a title
plt.title("Stripplot of Total Bill by Day (Grouped by Sex)")

# Show the plot
plt.show()
