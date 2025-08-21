import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
data = sns.load_dataset("tips")

# Create figure with specific size
plt.figure(figsize=(8, 5))  # Width=8 inches, Height=5 inches

# Create a barplot
sns.barplot(
    data=data,              # Dataset to be used
    x="day",                # Categorical variable on x-axis
    y="total_bill",         # Numerical variable on y-axis
    hue="sex",              # Split by gender
    palette="Set2",         # Color palette: 'Set2' is soft and readable
    ci="sd",                # Show standard deviation as error bars
    capsize=0.1,            # Add caps to error bars
    errcolor="black",       # Color of error bars
    errwidth=1.5            # Width of error bars
)

# Add title and axis labels with font size and color
plt.title("Average Total Bill by Day and Gender", fontsize=14, color="navy")     # Main title
plt.xlabel("Day", fontsize=12, color="green")                                    # X-axis label
plt.ylabel("Total Bill", fontsize=12, color="maroon")                            # Y-axis label

# Rotate x-axis labels
plt.xticks(rotation=25)  # Rotate x-axis tick labels 25 degrees for better readability

# Show gridlines
plt.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)  # Add horizontal dashed grid lines

# Show the final plot
plt.tight_layout()  # Adjust layout to prevent overlapping text
plt.show()
