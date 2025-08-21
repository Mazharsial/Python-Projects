import matplotlib.pyplot as plt
import numpy as np

# x=[1,2,3,4]
# y=[5,6,7,8]
# c=["red","blue","green","yellow"] # Giving Multiple colors

# plt.title("BarPlot", fontsize=15)
# plt.xlabel("Numbers", fontsize=15)
# plt.ylabel("Days", fontsize=15)

# plt.bar(x,y, width=0.4, color=c, align="edge" , edgecolor="r",linewidth=5, linestyle=":",alpha=0.4,label="Popularity") #align="centre", alpha-> for doing color light or blur
# plt.legend()
# plt.show()


# ******************************************************

# Drawing more than one bar graph in a single graph

# Sample data
labels = ['A', 'B', 'C', 'D']
values1 = [10, 15, 20, 25]  # First bar set
values2 = [5, 10, 15, 10]   # Second bar set

x = np.arange(len(labels))  # the label locations
width = 0.35  # width of the bars

# Create the plot
plt.bar(x - width/2, values1, width, label='Group 1', color='skyblue') # x - width/2 ->for setting position of first group to left side
plt.bar(x + width/2, values2, width, label='Group 2', color='orange')  # x + width/2 ->for setting position of second group to right side
# For horizontal Bar graph just we have to change plt.bar() to plt.barh()

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Two Bar Graphs in One Plot')
plt.xticks(x, labels, rotation=20)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
