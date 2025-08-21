import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from Seaborn (you can also use GitHub CSV version)
data = sns.load_dataset("tips")

# Create a Violin Plot
sns.violinplot(
    data=data,        # The full DataFrame
    x="day",          # Categorical variable (x-axis)
    y="total_bill",   # Numerical variable (y-axis)
    hue="sex",        # Optional: adds another categorical separation
    split=True,       # Splits the violin by hue groups (only if hue is set)
    inner="quartile", # Shows quartile lines inside the violin ('box', 'quartile', 'point', 'stick', or None)
    palette="Set2",   # Sets the color palette
    linewidth=1.2,    # Line width of the violin border
    scale="count"     # Scale by 'area', 'count', or 'width'
)

# Add title and display the plot
plt.title("Violin Plot of Total Bill by Day and Sex")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()
