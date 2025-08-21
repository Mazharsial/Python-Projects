import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset directly from GitHub
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
data = pd.read_csv(url)
# data=sns.load_dataset("penguins") # Direct method

# Display first few rows
print(data.head())

# Create a line plot
sns.lineplot(
    data=data,             # DataFrame containing the data
    x="bill_length_mm",    # Variable for x-axis
    y="bill_depth_mm",     # Variable for y-axis
    hue="species",         # Group lines by species using different colors
    style="sex",           # Different line styles (dashed, solid) for male/female
    markers=True,          # Show markers on each data point
    dashes=False,          # Use solid lines instead of dashed by default
    palette="Set2",        # Set color palette
    linewidth=2.5          # Width of the lines
)
# Seaborn provides default title and labels but
# If you want to add your own title or labels then consider below code:
# Add title and axis labels
plt.title("Line Plot of Bill Length vs Depth by Species and Sex")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")

# Show the plot
plt.show()

# ===========================
# Seaborn 'palette' Parameter Guide
# ===========================

# The `palette` parameter in Seaborn controls the color theme for plots.
# It can take a string (for built-in palettes), a list of color codes, a dictionary,
# or a callable function returning a color palette.

# ---------------------------------------------------
# 1. Built-in Named Palettes (Qualitative/Categorical)
# ---------------------------------------------------
# These are best for distinguishing different categories (non-numeric values):
#
# "deep"        - Default Seaborn palette (bold and balanced)
# "muted"       - Soft but rich colors
# "pastel"      - Very soft and light colors
# "bright"      - Highly saturated colors
# "dark"        - Dark and vivid colors
# "colorblind"  - Colorblind-safe colors
# "Set1"        - Matplotlib's bright color set
# "Set2"        - Softer colors than Set1
# "Set3"        - More variety, soft colors
# "tab10"       - 10-category color set from matplotlib
# "Accent"      - Alternative bold colors
# "Paired"      - 12 paired categorical colors
# "Pastel1", "Pastel2" - Very light pastel schemes

# ---------------------------------------------------
# 2. Sequential Palettes (Good for numeric progression)
# ---------------------------------------------------
# These range from light to dark (or vice versa):
#
# "Blues"       - Light to dark blue
# "Greens"      - Light to dark green
# "Oranges"     - Light to dark orange
# "Reds"        - Light to dark red
# "Purples"     - Light to dark purple
# "BuGn"        - Blue to green
# "YlGnBu"      - Yellow to green to blue