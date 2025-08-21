import matplotlib.pyplot as plt
import numpy as np

# Solid sample data
x = np.arange(0, 10, 1)        # x-axis values: 0 to 9
y = np.array([2, 4, 6, 5, 7, 3, 8, 6, 4, 5])  # Fixed y-axis values

# Create the stem plot
markerline, stemlines, baseline = plt.stem(
    x,         # x positions of the stems
    y,         # y values for stem heights

    # ---------------------------
    linefmt='g--',     
    # Format for stem lines (vertical lines from baseline to y value)
    # Format string = color + line style:
    #   Colors: 'r' = red, 'g' = green, 'b' = blue, 'k' = black, etc.
    #   Line styles: '-' = solid, '--' = dashed, '-.' = dash-dot, ':' = dotted
    # Examples: 'b-', 'g--', 'k:', 'r-.'

    markerfmt='ro',    
    # Format for data point markers (on top of each stem)
    # Format string = color + marker type:
    #   Colors: 'r', 'g', 'b', 'c', 'm', 'y', 'k', etc.
    #   Marker styles:
    #       'o' = circle, 's' = square, '^' = triangle_up,
    #       'D' = diamond, '*' = star, 'x' = cross, '+' = plus
    # Examples: 'ro' = red circle, 'gs' = green square, 'b^' = blue triangle

    basefmt='k-',       
    # Format for the baseline (horizontal line from which stems rise)
    # Format string: same rules as linefmt
    # Example: 'k-' = black solid, 'g--' = green dashed

    bottom=0,           
    # Where the baseline lies (vertical offset for the stem start)
    #   - Default is 0
    #   - You can raise/lower stems by setting bottom to another value
    # Example: bottom=-2 will start all stems from y=-2

    label='Sales Data'  
    # Label to be shown in legend
    # Can be any string like 'Temperature', 'Revenue', etc.
)

# Add x and y axis labels
plt.xlabel("Day")           # Label for x-axis
plt.ylabel("Units Sold")    # Label for y-axis

# Title of the chart
plt.title("Stem Chart of Sales Over 10 Days")

# Show legend (uses label from plt.stem)
plt.legend()

# Display the chart
plt.show()
