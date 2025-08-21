import matplotlib.pyplot as plt

# Solid data (e.g., exam scores or measurements)
data = [65, 70, 68, 75, 80, 85, 70, 72, 78, 90, 88, 85, 95]

# Create a box plot
plt.boxplot(
    [data],                     # Data should be inside a list even if it's one dataset
    # notch=True,                 # Draw a notch to show median CI
    widths=0.4,                 # Width of the box
    labels=['Test Scores'],     # Label below the box
    patch_artist=True,          # Allows coloring the box
    showmeans=True,             # Show the mean value with a marker
    whis=1.5,                   # Whiskers extend to 1.5 * IQR (default)
    sym='ro',                   # Red circles for outliers

    # Style dictionaries for customization:
    # boxprops=dict(facecolor='lightblue', color='black', linewidth=1.5),
    # capprops=dict(color='green', linewidth=1.2),
    # whiskerprops=dict(color='orange', linewidth=1.2, linestyle='--'),
    # flierprops=dict(marker='o', markerfacecolor='red', markersize=6, linestyle='none'),
    # medianprops=dict(color='red', linewidth=2),
    # meanprops=dict(marker='D', markerfacecolor='purple', markeredgecolor='black')
)

# Add labels and grid
plt.title("Box Plot of Test Scores")
plt.ylabel("Score")
plt.grid(True)

# Show the plot
plt.show()
