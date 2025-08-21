import matplotlib.pyplot as plt

# Static data
x = [8, 6, 20, 30, 22, 92, 84, 36, 59, 85, 62, 77, 76, 59, 92, 77, 63, 24, 86, 49, 
     43, 95, 73, 92, 93, 14, 58, 35, 49, 6, 83, 74, 87, 90, 69, 66, 52, 35, 10, 17, 
     84, 85, 94, 46, 9, 74, 19, 17, 38, 39]

# Create histogram
plt.hist(
    x,
    bins=10,                    # Number of bins (bars)
    range=(0, 100),             # Value range to consider
    edgecolor='black',          # Border color of bars
    color='skyblue',            # Fill color of bars
    bottom=0,                   # Shift bars from baseline (useful for stacking)
    align='mid',                # Align bars: 'left', 'mid', or 'right'
    histtype='bar',             # Histogram type: 'bar', 'barstacked', 'step', 'stepfilled'
    # orientation='horizontal',   # Horizontal orientation of bars
    rwidth=0.9,                  # Relative width (0.0 to 1.0); 1 = no spacing
    label="Population"
)

# Add grid lines
plt.grid(True)  # Enables grid for better readability (can also set axis, linestyle, alpha)

# Add vertical line to show mean
mean_value = sum(x) / len(x)
plt.axvline(
    mean_value,               # Position of the vertical line
    color='red',              # Line color
    label=f'Mean: {mean_value:.2f}'  # Label shown in legend
    # You can also use: linestyle, linewidth, alpha, etc.
)

# Add labels and legend
plt.title('Histogram with Grid, rwidth, and axvline')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()  # Show legend for the vertical line

# Show the plot
plt.show()
