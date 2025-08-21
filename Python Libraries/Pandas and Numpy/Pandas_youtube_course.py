import pandas as pd
# import numpy as np

# --------------------------------------------
# 0 -> Row-wise function execution
# 1 -> Column-wise function execution
# --------------------------------------------

# --------------------------------------------
# 1. Create a Series from a list
# --------------------------------------------
s1 = pd.Series([10, 20, 30])  # Series with default integer index
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])  # Series with custom index
print("1. Series from list:")
print(s1)

# --------------------------------------------
# 2. Create a Series from a dictionary
# --------------------------------------------
s2 = pd.Series({'a': 1, 'b': 2, 'c': 3})
print("\n2. Series from dictionary:")
print(s2)

# --------------------------------------------
# 3. Create a DataFrame from two Series
# --------------------------------------------
df1 = pd.DataFrame({'s1': [1, 2], 's2': [3, 4]})
print("\n3. DataFrame from two Series:")
print(df1)

# --------------------------------------------
# 4. Create a DataFrame from a dictionary
# --------------------------------------------
df2 = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30], 'language': ['c', 'python']})
print("\n4. DataFrame from dictionary:")

# Selecting specific columns and assigning custom index
var = pd.DataFrame(df2, columns=['name', 'age'], index=['a', 'b'])
print(var)

# Another correct way to change the index
var = df2[['name', 'age']]           # Select columns
var.index = ['a', 'b']               # Assign custom index
print(var)

# --------------------------------------------
# 5. Arithmetic Operations on DataFrame columns
# --------------------------------------------
var = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})

# Addition
var["c"] = var["A"] + var["B"]
print(var)

# Subtraction
var["c"] = var["A"] - var["B"]
print(var)

# Multiplication
var["c"] = var["A"] * var["B"]
print(var)

# Division
var["c"] = var["A"] / var["B"]
print(var)

# --------------------------------------------
# 6. Logical Operations (True/False based on condition)
# --------------------------------------------
var["python"] = var["A"] <= 2
print(var)

# --------------------------------------------
# 7. Insert and Remove Columns
# --------------------------------------------
# Insert column at specific position
var.insert(1, "D", var["A"])
print(var)

# Insert limited data
var["python"] = var["A"][:3]
print(var)

# Remove column using pop
var1 = var.pop("B")
print(var1)

# Remove column using del
# del var["B"]
# print(var)

# --------------------------------------------
# 8. Writing DataFrame to CSV
# --------------------------------------------
var = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
var.to_csv("test.csv")
var.to_csv("test_1.csv", index=False)  # Without index
var.to_csv("test_2.csv", index=False, header=[1, 2])  # Custom headers

# --------------------------------------------
# 9. Reading a CSV file
# --------------------------------------------
# Use appropriate path to read the CSV file

# csv_1 = pd.read_csv("sample_employees.csv")
# print(csv_1)

# Read first 2 rows
# csv_2 = pd.read_csv("sample_employees.csv", nrows=2)
# print(csv_2)

# Read specific columns
# csv_3 = pd.read_csv("sample_employees.csv", usecols=["Name", "Department"])
# print(csv_3)

# Read columns by index
# csv_4 = pd.read_csv("sample_employees.csv", usecols=[0, 1, 2])
# print(csv_4)

# Skip specific rows
# csv_5 = pd.read_csv("sample_employees.csv", skiprows=[0, 1])
# print(csv_5)

# Change index column
# csv_6 = pd.read_csv("sample_employees.csv", index_col=["Name"])
# print(csv_6)

# Set a row as header
# csv_7 = pd.read_csv("sample_employees.csv", header=[1])
# print(csv_7)

# Give custom headers
# csv_8 = pd.read_csv("sample_employees.csv", names=["Employee", "Age_2", "Department_2", "Salary_2", "Joining_Date_2"])
# print(csv_8)

# Make header none
# csv_9 = pd.read_csv("sample_employees.csv", header=None)
# print(csv_9)

# Change data type of column
# csv_10 = pd.read_csv("sample_employees.csv", dtype={"Salary": "float"})
# print(csv_10)

# Print column names
# print(csv_10.columns)

# Print summary statistics
# print(csv_10.describe())

# Print first and last few rows
# print(csv_10.head(2))
# print(csv_10.tail())

# Access index
# print(csv_10.index.array)

# Convert to NumPy array
# print(csv_10.to_numpy())

# Convert entire DataFrame to NumPy using asarray
# l = np.asarray([csv_10])
# print(l)

# Sort index
# print(csv_10.sort_index(axis=0, ascending=False))

# --------------------------------------------
# 10. Modify specific cell value
# --------------------------------------------
# csv_10.loc[0, "Name"] = "Mazhar"
# print(csv_10)

# Get specific data using loc
# print(csv_10.loc[[0, 2], ["Name", "Age"]])

# Drop columns or rows
# print(csv_10.drop("Age", axis=1))
# print(csv_10.drop(0, axis=0))

# --------------------------------------------
# 11. Handling Missing Values
# --------------------------------------------
# Drop rows with any or all missing values
# print(csv_10.dropna())
# print(csv_10.dropna(how='any'))
# print(csv_10.dropna(how='all'))  # Drop row if all values are NaN

# Drop rows with threshold
# print(csv_10.dropna(thresh=1))

# Fill missing values
# print(csv_10.fillna("python"))
# print(csv_10.fillna({"Name": "Mazhar", "Age": 18}))
# print(csv_10.fillna(method="ffill"))
# print(csv_10.fillna(method="bfill"))
# print(csv_10.fillna(method="ffill", axis=0))
# print(csv_10.fillna(method="bfill", axis=1))
# csv_10.fillna(12, inplace=True)
# print(csv_10)
# print(csv_10.fillna("python", limit=2))

# --------------------------------------------
# 12. Replace values
# --------------------------------------------
# print(csv_10.replace(to_replace="Bob", value="David"))
# print(csv_10.replace(["Alice", "Bob"], 5))
# Replace using regex
# print(csv_10.replace("[A-Za-z]", "Python", regex=True))
# Replace using dictionary and regex
# print(csv_10.replace({"Name": "[A-Za-z]"}, "Mazhar", regex=True))

# --------------------------------------------
# 13. Read and summarize CSV file (data.csv)
# --------------------------------------------
try:
    df_csv = pd.read_csv('data.csv')
    print("\n5. First 5 rows of data.csv:")
    print(df_csv.head())

    print("\n6. DataFrame info:")
    print("Column names:", df_csv.columns.tolist())
    print("\nData types:")
    print(df_csv.dtypes)
    print("\nSummary statistics:")
    print(df_csv.describe())
except FileNotFoundError:
    print("\nFile 'data.csv' not found - skipping this example")

# --------------------------------------------
# 14. Sample DataFrame for cleaning examples
# --------------------------------------------
data = {
    'A': [1, 2, None, 4],
    'B': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
    'age': [25, -30, 35, 40],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie']
}
df_clean = pd.DataFrame(data)

# Fill empty cells with default value
df_clean['A'] = df_clean['A'].fillna(0)
print("\n7. After filling empty cells:")
print(df_clean)

# Convert date column to datetime
df_clean['B'] = pd.to_datetime(df_clean['B'])
print("\n8. After converting to datetime:")
print(df_clean.dtypes)

# Replace negative ages with mean of positive ages
mean_age = df_clean.loc[df_clean['age'] > 0, 'age'].mean()
df_clean['age'] = df_clean['age'].apply(lambda x: mean_age if x < 0 else x)
print("\n9. After replacing negative ages:")
print(df_clean)

# Remove duplicate rows
df_clean = df_clean.drop_duplicates()
print("\n10. After removing duplicates:")
print(df_clean)
