import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------------------
# Step 1: Load the penguins dataset from GitHub
# -----------------------------------------
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
data = pd.read_csv(url)

# Drop missing values to avoid plotting issues
data = data.dropna()

# -----------------------------------------
# Step 2: Create a histogram using Seaborn
# -----------------------------------------
sns.histplot(
    data=data,                  # The DataFrame containing your data
    x="flipper_length_mm",      # Column to plot on the x-axis (the variable you're analyzing)
    bins=20,                    # Number of bins (intervals). Default is auto-calculated
    kde=True,                   # If True, overlays a KDE (Kernel Density Estimate) line
    rug=True,                   # If True, adds small vertical lines under x-axis for each point
    hue="species",              # Group the histogram by species using different colors
    multiple="stack",           # 'stack', 'dodge', 'layer', or 'fill' — controls how hues are shown
    stat="count",               # 'count', 'frequency', 'density', or 'probability'
    element="bars",             # 'bars', 'step', or 'poly' — shape of histogram
    fill=True,                  # If True, fill the bars with color; if False, only outlines
    palette="Set2",             # Color palette used to differentiate groups
    edgecolor="black",          # Border color of the bars
    linewidth=0.5               # Width of the bar edges
)

# -----------------------------------------
# Step 3: Add titles and labels
# -----------------------------------------
plt.title("Histogram of Flipper Length by Penguin Species")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Count")

# Show the plot
plt.show()
