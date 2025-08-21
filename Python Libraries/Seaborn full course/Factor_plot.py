import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'tips' dataset
# GitHub link: https://github.com/mwaskom/seaborn-data/blob/master/tips.csv
data = sns.load_dataset("tips")

# Create a categorical plot (replacement for deprecated 'factorplot')
sns.catplot(
    data=data,             # DataFrame to plot
    x="day",               # Categorical axis
    y="total_bill",        # Numerical axis
    hue="sex",             # Optional grouping
    kind="box",            # Type of plot: box, violin, bar, strip, swarm, point, etc.
    col="time",            # Create separate subplots (facets) for each time (Lunch/Dinner)
    row="smoker",          # Additional facet layer (optional)
    palette="Set2",        # Color palette
    height=4,              # Height of each facet
    aspect=1,              # Aspect ratio (width = height * aspect)
    dodge=True             # Separate plots for each hue level
)

# Add a title (you can only do this outside catplot)
plt.subplots_adjust(top=0.9)  # Adjust the top of the figure to fit the title
plt.suptitle("Catplot of Total Bill by Day, Time, Sex, and Smoking Status")

# Show the plot
plt.show()
