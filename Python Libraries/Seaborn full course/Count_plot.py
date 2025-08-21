import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'tips' dataset (also available on GitHub: https://github.com/mwaskom/seaborn-data/blob/master/tips.csv)
data = sns.load_dataset("tips")

# Create a countplot
sns.countplot(
    data=data,         # Dataset to plot
    x="day",           # Categorical variable to count (x or y required)
    hue="sex",         # Optional categorical variable to split bars (e.g., by gender)
    palette="pastel",  # Set color palette ('deep', 'muted', 'pastel', 'dark', etc.)
    order=["Thur", "Fri", "Sat", "Sun"],  # Custom order of categories
    dodge=True,        # Separate the bars for different hue levels (default: True)
    saturation=0.8,    # Color saturation (0 = grayscale, 1 = full color)
    edgecolor="black", # Color of bar borders
    linewidth=1        # Width of bar borders
)

# Add a title
plt.title("Countplot of Visits per Day (Grouped by Sex)")

# Show the plot
plt.show()
