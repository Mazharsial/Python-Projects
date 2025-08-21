import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from Seaborn (also available on GitHub: https://github.com/mwaskom/seaborn-data/blob/master/tips.csv)
data = sns.load_dataset("tips")

# Create a Pairplot
sns.pairplot(
    data=data,         # DataFrame containing the data
    hue="sex",         # Color the plots by 'sex' column
    palette="husl",    # Color palette (e.g., 'husl', 'Set1', 'muted', etc.)
    diag_kind="kde",   # Type of plot on the diagonal: 'hist' or 'kde'
    kind="scatter",    # Kind of plot off-diagonal: 'scatter' or 'kde'
    markers=["o", "s"],# Markers for different hue levels
    corner=False       # If True, plots only lower triangle (saves space)
)

# Show the plot
plt.suptitle("Pairplot of Tips Dataset", y=1.02)
plt.show()
