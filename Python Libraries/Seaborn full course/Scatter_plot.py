import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------------------
# Step 1: Load the penguins dataset from GitHub
# -----------------------------------------
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
data = pd.read_csv(url)

# Drop missing values to ensure clean plotting
data = data.dropna()

# -----------------------------------------
# Step 2: Create a scatterplot using Seaborn
# -----------------------------------------
sns.scatterplot(
    data=data,                     # DataFrame with your data
    x="bill_length_mm",           # X-axis variable (numeric)
    y="bill_depth_mm",            # Y-axis variable (numeric)
    hue="species",                # Color coding by category (e.g., species)
    style="sex",                  # Marker style based on a categorical variable (e.g., male/female)
    size="body_mass_g",           # Size of each point based on a numeric variable
    palette="Set2",               # Color palette
    sizes=(20, 200),              # Min and max point size range
    marker="o",                   # Shape of the marker (e.g., 'o', '^', 's', etc.)
    edgecolor="black",            # Border color around markers
    linewidth=0.5,                # Width of the edge border
    alpha=0.8                     # Transparency of points (0=transparent, 1=opaque)
)

# -----------------------------------------
# Step 3: Add labels and title
# -----------------------------------------
plt.title("Penguins: Bill Length vs Bill Depth")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")

# Show the plot
plt.show()
