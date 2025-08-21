import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'tips' dataset from seaborn (also on GitHub)
data = sns.load_dataset("tips")

# Create a catplot (categorical plot, general-purpose function)
sns.catplot(
    data=data,            # The DataFrame to be plotted
    x="day",              # Categorical variable on X-axis
    y="total_bill",       # Numerical variable on Y-axis
    kind="box",           # Type of plot: 'strip', 'swarm', 'box', 'violin', 'bar', 'point', 'count'
    hue="sex",            # Optional: split the data by gender using different colors
    col="time",           # Create separate subplots for each value of 'time' (Lunch/Dinner)
    row="smoker",         # Optional: create another row of subplots by smoker status
    palette="pastel",     # Color theme for the plot ('deep', 'muted', 'Set2', 'pastel', etc.)
    dodge=True,           # If True, separates the hue categories side by side
    height=4,             # Height of each subplot
    aspect=1.2            # Width-to-height ratio of each subplot
)

# Add a title to the overall figure (catplot returns a FacetGrid)
plt.subplots_adjust(top=0.9)              # Adjust space for title
plt.suptitle("Catplot of Total Bill by Day, Time, Sex, and Smoker")

# Show the plot
plt.show()
