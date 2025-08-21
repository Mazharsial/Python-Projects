import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
data = sns.load_dataset("penguins")

# Compute correlation matrix (only for numeric columns)
corr = data.corr(numeric_only=True)

# Create heatmap
sns.heatmap(
    corr,                  # Data
    annot=True,            # Show values in cells
    cmap="coolwarm",       # Color palette
    linewidths=0.5,        # Line width between boxes
    linecolor='gray',      # Color of lines
    square=True,           # Make cells square
    cbar=True              # Show color bar (legend)
)

plt.title("Correlation Heatmap - Penguins Dataset")
plt.show()
