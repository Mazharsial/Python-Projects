import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------------------
# Step 1: Load penguins dataset from GitHub
# -----------------------------------------
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
data = pd.read_csv(url)

# Drop rows with missing values to avoid errors in plotting
data = data.dropna()

# -----------------------------------------
# Step 2: Create a bar plot using Seaborn
# -----------------------------------------
sns.barplot(
    data=data,                   # The DataFrame containing the data
    x="species",                 # Categorical variable for x-axis
    y="flipper_length_mm",       # Numeric variable to aggregate on y-axis
    hue="sex",                   # (Optional) Adds color grouping by 'sex'
    estimator="mean",            # Aggregation function: mean, median, count, etc.
    errorbar="sd",               # Type of error bar: 'sd', 'ci', or None
    palette="Set2",              # Color scheme for different hue categories
    dodge=True,                  # If True, separates bars by hue; if False, overlaps them
    capsize=0.1,                 # Adds caps on error bars (0 to 1 scale)
    errwidth=1.5,                # Width of error bars
    linewidth=1,                 # Border line width of bars
    edgecolor="black"            # Color of bar edges
)

# -----------------------------------------
# Step 3: Add title and axis labels
# -----------------------------------------
plt.title("Average Flipper Length by Species and Sex")
plt.xlabel("Penguin Species")
plt.ylabel("Flipper Length (mm)")

# Show the plot
plt.show()
