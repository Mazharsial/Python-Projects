
# NumPy Course Notes

# 1. Creating a NumPy Array
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2. Input Array from User
# Convert input list to NumPy array
# list1 = list(eval(input("Enter list elements (like [1, 2, 3]): ")))
# arr = np.array(list1)
# print(arr)

# 3. Basic Array Operations
print("Sum:", np.sum(arr))          # Calculates sum of all elements
print("Mean:", np.mean(arr))        # Calculates mean (average)
print("Max:", np.max(arr))          # Finds maximum value
print("Min:", np.min(arr))          # Finds minimum value

# Multiply each element by 2
new_arr = arr * 2
print("Array after multiplication:", new_arr)

# 4. 2D Array from List
# Convert a list into 2D array using reshape
my_list = [1, 2, 3, 4, 5, 6]
arr_2d = np.array(my_list).reshape(2, 3)
print("2D Array:")
print(arr_2d)

# 5. Create Diagonal Matrix
arr = np.zeros((3, 3), dtype=int)     # Initialize 3x3 array with zeros
np.fill_diagonal(arr, 1)              # Fill the diagonal with ones
print("Ones on diagonal:\n", arr)

# 6. Create 2D Array Using Range
# Create list using range
my_list = list(range(1, 13))
arr_2d = np.array(my_list).reshape(3, 4)
print("2D Array:")
print(arr_2d)

# 7. NumPy Array Attributes
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
print("Shape:", arr.shape)       # Shape of array
print("Dimensions:", arr.ndim)   # Number of dimensions
print("Size:", arr.size)         # Total number of elements
print("Data type:", arr.dtype)   # Data type of elements
print("Item size:", arr.itemsize) # Bytes per element
print("Total bytes:", arr.nbytes) # Total bytes used

# 8. Slicing in 2D Arrays
arr_2d = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]])
print("Original 2D Array:\n", arr_2d)

# Get subarray from 2nd row and 2nd & 3rd columns
slice_1 = arr_2d[1:2, 1:3]  
print("\nFirst two rows, first three columns:\n", slice_1)

# 9. Element-wise Operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# 10. Random Numbers in NumPy
from numpy import random

# Single random integer
print(random.randint(100))

# Random float array (3x5)
print(random.rand(3, 5))

# Random choice from list in 3x5 array
print(random.choice([3, 5, 7, 9], size=(3, 5)))

# 11. NumPy Array Data Types
# Integer array
int_array = np.array([1, 2, 3])
print("Integer array dtype:", int_array.dtype)

# Float array
float_array = np.array([1.1, 2.2, 3.3])
print("Float array dtype:", float_array.dtype)

# String array
string_array = np.array(['a', 'b', 'c'])
print("String array dtype:", string_array.dtype)

# 12. Convert Array Data Type
arr = np.array([0, 1, 2, 3, 4])
float32_arr = arr.astype(np.float32)
print("Original array:", arr)
print("Converted to float32:", float32_arr)
print("Dtype of new array:", float32_arr.dtype)

# 13. Iteration Over Arrays
# 1D Array
arr1d = np.array([10, 20, 30, 40])
for element in arr1d:
    print("Element:", element)

# 2D Array row-wise
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for row in arr2d:
    print("Row:", row)

# Using nditer for any dimensional array
for val in np.nditer(arr2d):
    print("Element:", val)

# 14. Additional Slicing Examples
# Get second row
print("\nSecond row:", arr_2d[1, :])  
# Get third column
print("\nThird column:", arr_2d[:, 2])  
# Reverse rows
print("\nReversed rows:\n", arr_2d[::-1, :])
# Reverse columns
print("\nReversed columns:\n", arr_2d[:, ::-1])
# Bottom-right 2x2
print("\nBottom-right 2x2 submatrix:\n", arr_2d[1:, 2:])

# 15. Matrix Multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = A @ B
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nMatrix Multiplication (A @ B):\n", result)

# 16. Sorting
arr = np.array([10, 5, 8, 2, 7, 3])
sorted_arr = np.sort(arr)
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)

# 17. Timing with %timeit (in Jupyter Only)
# NOTE: %timeit only works inside Jupyter or IPython environments
# So it's commented out here to avoid error in script
# %timeit np.arange()
