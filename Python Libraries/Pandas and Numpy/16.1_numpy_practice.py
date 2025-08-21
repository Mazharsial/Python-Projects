import numpy as np

# Sales data in lacs (2019–2023) with Restaurant ID in first column
sales_data = np.array([
    [0, 120, 100, 150, 180, 200],  # R000 - Spicy Grill
    [1,  80, 120, 140, 160, 190],  # R001 - Foodie's Heaven
    [2, 100, 110, 130, 170, 220],  # R002 - Biryani House
    [3, 140, 130, 160, 200, 250],  # R003 - Pizza Spot
    [4,  90, 100, 110, 140, 160],  # R004 - BBQ Palace
])

# 🔸 Displaying the complete sales dataset
print("📊 Full Sales Data (including IDs):\n", sales_data)

# 🔹 Extracting and printing 2023 sales (last column)
print("\n📅 Sales for the year 2023:\n", sales_data[:, 5])

# 🔹 Average sales of each restaurant across 5 years
average_sales = np.average(sales_data[:, 1:], axis=1)
print("\n📈 Average sales of each restaurant (2019–2023):\n", average_sales)

# 🔹 Sales data for Pizza Spot (ID = 3)
print("\n🍕 Sales of R003 - Pizza Spot across 5 years:\n", sales_data[3, 1:])

# 🔹 Maximum sales of each restaurant (highest year for each)
max_sales = np.max(sales_data[:, 1:], axis=1)
print("\n🔺 Maximum single-year sales of each restaurant:\n", max_sales)

# 🔹 Restaurants that had sales above 200 lacs in any year
above_sales = np.where(np.any(sales_data[:, 1:] > 200, axis=1))[0]
print("\n🚀 Restaurants with sales above 200 lacs in any year (indexes):\n", above_sales)

# 🔹 Year-wise maximum sales
print("\n🏆 Maximum sales in each year (2019–2023):\n", np.max(sales_data[:, 1:], axis=0))

# 🔹 Replace all sales below 120 lacs with 0 (keep ID column intact)
replaced_sales = np.copy(sales_data)
replaced_sales[:, 1:] = np.where(sales_data[:, 1:] > 120, sales_data[:, 1:], 0)
print("\n🧹 Sales data with all values below 120 replaced by 0:\n", replaced_sales)

# 🔹 Sum of all restaurants' sales year-wise (2019 to 2023)
sum_one_year = np.sum(sales_data[:, 1:], axis=0)
print("\n➕ Total sales across all restaurants for each year:\n", sum_one_year)

# 🔹 Minimum sales year-wise and corresponding restaurant indexes
min_one_year = np.min(sales_data[:, 1:], axis=0)
min_one_year_index = np.argmin(sales_data[:, 1:], axis=0)
print("\n🔻 Minimum sales in each year:\n", min_one_year)
print("\n🧭 Indexes of restaurants with minimum sales in each year:\n", min_one_year_index)

# 🔹 Cumulative sum of sales for each restaurant across years
cumulative_sum = np.cumsum(sales_data[:, 1:], axis=1)
print("\n📈 Cumulative sales per restaurant over years:\n", cumulative_sum)

# 🔹 Mean sales of each restaurant
mean_sales = np.mean(sales_data[:, 1:], axis=1)
print("\n📊 Mean sales of each restaurant (2019–2023):\n", mean_sales)
