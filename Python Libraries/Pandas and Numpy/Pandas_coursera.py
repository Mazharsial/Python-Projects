import pandas as pd

# Create a sample Series with custom index
# Series is a one-dimensional labeled array (like a column in Excel)
data = pd.Series([10, 20, 30, 20, None, 50, 10], 
                 index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# 1. values attribute
# Returns the underlying data as a NumPy array (without index)
print("Values as NumPy array:")
print(data.values)  # Output: [10. 20. 30. 20. nan 50. 10.]
print("\n")

# 2. index attribute
# Returns the index object containing axis labels
print("Index labels:")
print(data.index)  # Output: Index(['a', 'b', 'c', 'd', 'e', 'f', 'g'], dtype='object')
print("\n")

# 3. shape attribute
# Returns a tuple representing the dimensionality (single value for Series)
print("Shape (number of elements):")
print(data.shape)  # Output: (7,) - 7 elements
print("\n")

# 4. size attribute
# Returns number of elements (including NaN/None values)
print("Total elements (including missing):")
print(data.size)  # Output: 7
print("\n")

# 5. Summary statistics methods
# These automatically ignore missing values (None/NaN)
print("Mean (average):", data.mean())  # (10+20+30+20+50+10)/6
print("Sum:", data.sum())              # Sum of all non-null values
print("Minimum value:", data.min())    # Smallest non-null value
print("Maximum value:", data.max())    # Largest non-null value
print("\n")

# 6. unique() and nunique() methods
# unique() - returns distinct values (including NaN if present)
# nunique() - counts number of distinct values (excluding NaN by default)
print("Unique values:", data.unique())  # [10. 20. 30. nan 50.]
print("Number of unique values (excluding None):", data.nunique())  # 4
print("\n")

# 7. sort_values() and sort_index() methods
# sort_values() - orders by values (ascending by default)
# sort_index() - orders by index labels
print("Sorted by values (ascending):\n", data.sort_values())
print("\nSorted by index (alphabetical):\n", data.sort_index())
print("\nSorted by values (descending):\n", data.sort_values(ascending=False))
print("\n")

# 8. isnull() and notnull() methods
# Boolean masks identifying missing/non-missing data
print("Is Null (missing values):\n", data.isnull())  # True for index 'e'
print("\nNot Null (existing values):\n", data.notnull())  # False for index 'e'
print("\n")

# 9. apply() method
# Applies a function to each element in the Series
# Here we square each value (while preserving None)
print("Apply square function:\n", 
      data.apply(lambda x: x**2 if pd.notnull(x) else x))
# Output: a:100, b:400, c:900, d:400, e:None, f:2500, g:100
print("\n")

# Bonus: Handling missing values
print("Count of non-null values:", data.count())  # 6 (excluding None)
print("\nFilling missing value with 0:\n", data.fillna(0))
print("\nDropping missing value:\n", data.dropna())


# -------------------------------------------------
# Pandas Datafram
# ---------------------------------------------------

import pandas as pd

# Creating the DataFrame from a dictionary
# Each key becomes a column, and values become row entries
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# 1. shape attribute
# Returns a tuple representing (number of rows, number of columns)
print("DataFrame shape (rows, columns):")
print(df.shape)  # Output: (4, 3) for 4 rows and 3 columns
print("\n")

# 2. info() method
# Provides concise summary of the DataFrame including:
# - Data types of each column
# - Number of non-null values
# - Memory usage
print("DataFrame info:")
print(df.info())  # Shows index dtype, column dtypes, non-null counts and memory usage
print("\n")

# 3. describe() method
# Generates descriptive statistics for numerical columns only (Age in this case)
# Includes count, mean, std, min, 25%, 50%, 75%, max
print("Summary statistics for numerical columns:")
print(df.describe())
print("\n")

# 4. head() and tail() methods
# head(n) - returns first n rows (default n=5)
# tail(n) - returns last n rows (default n=5)
print("First 2 rows:")
print(df.head(2))  # Shows first two rows
print("\nLast 2 rows:")
print(df.tail(2))  # Shows last two rows
print("\n")

# 5. Statistical methods
# These operate on Series (single columns)
print("Mean age:", df['Age'].mean())  # Calculates average age
print("Sum of ages:", df['Age'].sum())  # Sum of all ages
print("Minimum age:", df['Age'].min())  # Youngest age
print("Maximum age:", df['Age'].max())  # Oldest age
print("\n")

# 6. sort_values() method
# Sorts the DataFrame by specified column(s)
print("Sorted by Age (ascending by default):")
print(df.sort_values('Age'))  # Sorts by Age in ascending order
print("\nSorted by Name descending:")
print(df.sort_values('Name', ascending=False))  # Sorts by Name Z-A
print("\n")

# 7. groupby() method
# Groups data by specified column(s) for aggregation
# Adding a Salary column to make grouping more meaningful
df['Salary'] = [70000, 80000, 90000, 75000]
print("Average salary by city:")
print(df.groupby('City')['Salary'].mean())  # Groups by City, calculates mean Salary
print("\n")

# 8. Handling missing data and columns
# First create a missing value for demonstration
df.loc[1, 'Age'] = None  # Set Bob's age to missing

# fillna() - fills missing values with specified value
print("Filled missing values (with 0):")
print(df.fillna({'Age': 0}))  # Fills missing Age with 0

# dropna() - removes rows with missing values
print("\nDropping rows with missing values:")
print(df.dropna())  # Removes row with missing Age (Bob)

# rename() - changes column names
print("\nRenaming columns:")
print(df.rename(columns={'Name': 'Full Name', 'Age': 'Years'}))  # Changes column names
print("\n")

# 9. apply() method
# Applies a function along an axis (columns or rows) of DataFrame
# or to elements of a Series

# Applying to a Series (Name column)
print("Names in uppercase:")
print(df['Name'].apply(lambda x: x.upper()))  # Converts each name to uppercase

# Applying to a Series with condition (Age column)
print("\nAge in dog years (Age * 7):")
print(df['Age'].apply(lambda x: x * 7 if pd.notnull(x) else None))  # Calculates "dog years"