import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (also available on GitHub: https://github.com/mwaskom/seaborn-data/blob/master/tips.csv)
data = sns.load_dataset("tips")

# Create a boxplot
sns.boxplot(
    data=data,          # DataFrame containing the data
    x="day",            # Categorical variable (e.g., days of the week)
    y="total_bill",     # Numeric variable to summarize
    hue="sex",          # Color grouping by a categorical variable (optional)
    palette="Set2",     # Color palette (e.g., 'Set1', 'husl', 'deep', 'muted', etc.)
    dodge=True,         # Separate boxplots for each level of hue (default: True)
    width=0.6,          # Width of each box
    linewidth=2,        # Width of lines around boxes and whiskers
    fliersize=5,        # Size of the outlier points (dots outside the whiskers)
    boxprops=dict(edgecolor='black'),         # Customize the box border
    whiskerprops=dict(color='black', linestyle='--'), # Customize whiskers
    capprops=dict(color='gray'),              # Customize the caps on whiskers
    medianprops=dict(color='red', linewidth=2),# Customize median line
)

# Add a title
plt.title("Boxplot of Total Bill by Day (Grouped by Sex)")

# Show the plot
plt.show()
