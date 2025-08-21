# import matplotlib.pyplot as plt

# # Data
# slices = [25, 35, 20, 20]
# labels = ['Apple', 'Banana', 'Mango', 'Grapes']
# colors = ['red', 'yellow', 'orange', 'green']
# explode = [0.1, 0, 0, 0]  # Explode 'Apple'

# # Create pie chart
# wedges, texts, autotexts = plt.pie(
#     slices,
#     labels=labels,                 # 🔹 Labels for each slice
#     colors=colors,                 # 🔹 Custom slice colors
#     explode=explode,               # 🔹 Pull out 'Apple' slice
#     autopct='%1.1f%%',             # 🔹 Show percentage values
#     startangle=45,                 # 🔹 Rotates pie (0 = right, 90 = top, etc.)
#     shadow=True,                   # 🔹 Adds shadow (3D look)
#     radius=1.2,                    # 🔹 Size of the pie
#     textprops={'fontsize': 12},    # 🔹 Label font size
#     wedgeprops={
#         'linewidth': 2,            # 🔹 Border thickness
#         'edgecolor': 'black'       # 🔹 Border color
#     },
#     counterclock=False,            # 🔹 Fill clockwise
#     labeldistance=1.1              # 🔹 Distance of labels from center (default: 1.1)
# )

# # Add legend
# plt.legend(wedges, labels, title="Fruits", loc=2)  # 🔹 loc=2 is upper left

# # Title
# plt.title("Fruit Distribution (Full Custom Pie Chart)")

# # Show plot
# plt.show()






import matplotlib.pyplot as plt

# Data
slices = [25, 35, 20, 20]
labels = ['Apple', 'Banana', 'Mango', 'Grapes']
colors = ['red', 'yellow', 'orange', 'green']

# Create ring (donut) pie chart
plt.pie(
    slices,
    labels=labels,                      # 🔹 Labels for slices
    colors=colors,                      # 🔹 Slice colors
    autopct='%1.1f%%',                  # 🔹 Show percentage values
    startangle=90,                      # 🔹 Rotate chart to start from top
    wedgeprops={'width': 0.4}           # 🔹 Width < 1 makes a ring (donut effect)
)

# Add title
plt.title("Fruit Distribution (Ring Pie Chart)")

# Show plot
plt.show()
