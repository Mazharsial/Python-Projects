import matplotlib.pyplot as plt

# Sample data
x = [10, 20, 30, 40, 50]
y = [5, 15, 25, 10, 30]
sizes = [100, 200, 300, 150, 250]

# Use a numeric variable to control color
colors = [1, 2, 3, 4, 5]  # This could be any metric (like temperature, score, etc.)

# Create scatter plot with colormap
scatter = plt.scatter(x, y,
                      c=colors,           # color based on data values
                      s=sizes,
                      cmap='viridis',     # colormap ('plasma', 'cool', 'rainbow', etc.)
                      alpha=0.8,
                      marker='o',
                      edgecolor='black')

# Add labels and title
plt.xlabel('X-axis Values')
plt.ylabel('Y-axis Values')
plt.title('Scatter Plot with Colormap and Colorbar')

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Color Intensity (based on values)')  # label for the colorbar

# Show plot
plt.grid(True)
plt.show()
