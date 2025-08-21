import numpy as np

# 1. Axis Basics
# axis=0: Operate vertically (down columns).
# axis=1: Operate horizontally (across rows).

# # ======================
# # 1. Array Creation
# # ======================

# # 1.1 Create 1D array with values 1-10
# arr1 = np.arange(1, 11)  # arange(start, stop, step) - similar to range() but returns array
# print("1.1:", arr1)

# # 1.2 Create 2D array shape (3,3) with values 1-9
# arr2 = np.arange(1, 10).reshape(3, 3)  # reshape() changes array dimensions
# print("\n1.2:", arr2)

# # 1.3 Check array shape compatibility
# a = np.array([1,2,3,4])
# b = np.array([4,2,6,1])
# print("\n1.3 Compatibility check:", a.shape == b.shape)  # shape returns dimensions tuple

# # ======================
# # 2. Special Arrays
# # ======================

# # 2.1 4x4 array of ones
# arr3 = np.ones((4, 4))  # Creates array filled with 1.0
# print("\n2.1 Ones array:\n", arr3)

# # 2.2 3x5 array of zeros
# arr4 = np.zeros((3, 5))  # Creates array filled with 0.0
# print("\n2.2 Zeros array:\n", arr4)

# # 2.3 Array filled with constant value
# full = np.full((2,3), 7)  # Creates array filled with specified value
# print("\n2.3 Full array:\n", full)

# # 2.4 Empty array (contains garbage values)
# arr5 = np.empty((2, 3))  # Allocates memory but doesn't initialize values
# print("\n2.4 Empty array:\n", arr5)

# # 2.5 Array with values 0-20 step 2
# arr6 = np.arange(0, 21, 2)  # Like range() but returns array
# print("\n2.5 Stepped array:\n", arr6)

# # 2.6 5x5 identity matrix
# arr7 = np.eye(5)  # Creates square identity matrix
# print("\n2.6 Identity matrix:\n", arr7)

# # ======================
# # 3. Random Number Arrays
# # ======================

# # 3.1 Uniform distribution [0,1)
# arr8 = np.random.rand(3, 3)  # rand() creates uniform random values
# print("\n3.1 Uniform random:\n", arr8)

# # 3.2 Standard normal distribution
# arr9 = np.random.randn(5)  # randn() creates normally distributed values
# print("\n3.2 Normal random:\n", arr9)

# # 3.3 Uniform distribution [0.0,1.0)
# arr10 = np.random.ranf(4)  # Alias for random_sample()
# print("\n3.3 Random floats:\n", arr10)

# # 3.4 Random integers
# arr11 = np.random.randint(10, 50, size=(2, 4))  # randint(low, high, size)
# print("\n3.4 Random integers:\n", arr11)

# # ======================
# # 4. Indexing & Slicing
# # ======================

# # 4.1 Access 3rd element (0-based)
# arr12 = np.array([10, 20, 30, 40, 50])
# print("\n4.1 Third element:", arr12[2])

# # 4.2 2D array access
# arr_2d = np.array([[1,2,3], [4,5,6]])
# print("\n4.2 2D element:", arr_2d[1,2])  # [row, column]

# # 4.3 Access entire row
# print("\n4.3 Entire row:", arr_2d[1])

# # 4.4 Access column
# print("\n4.4 Entire column:", arr_2d[:,1])

# # 4.5 Slice first three elements
# print("\n4.5 First three:", arr12[:3])

# # ======================
# # 5. Arithmetic Operations
# # ======================

# # 5.1 Array operations
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print("\n5.1 Arithmetic:")
# print("Addition:", a + b)  # Element-wise
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)  # Element-wise, not matrix multiplication
# print("Dot product:", np.dot(a, b))  # True vector multiplication

# # Dot Product of Vectors (1D arrays)
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Method 1: np.dot()
# dot_product = np.dot(a, b)  # 1*4 + 2*5 + 3*6 = 32

# # Method 2: @ operator (Python 3.5+)
# dot_product = a @ b  # Same result: 32

# # Method 3: np.sum(a * b)
# dot_product = np.sum(a * b)  # 32

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# # Dot Product of Matrix multiplication

# result = np.dot(A, B)  # Or A @ B
# # Output:
# # [[19 22]
# #  [43 50]]
# # Calculation:
# # 1*5 + 2*7 = 19 | 1*6 + 2*8 = 22
# # 3*5 + 4*7 = 43 | 3*6 + 4*8 = 50

# # ======================
# # 6. Sorting & Statistics
# # ======================

# # 6.1 Sort array
# arr15 = np.array([5, 2, 9, 1, 5, 6])
# print("\n6.1 Sorted:", np.sort(arr15))  # Returns new sorted array

# # 6.2 Sort 2D array by column
# arr_2d_col = np.array([[4,2,5],
#                        [7,1,2],
#                        [3,6,9]])
# print("\n6.2 Sorted by column:\n", np.sort(arr_2d_col, axis=0))  # axis=0 for columns

# # 6.3 Min/max operations
# arr16 = np.array([12, 45, 1, 67, 23])
# print("\n6.3 Statistics:")
# print("Min:", arr16.min(), "at index", arr16.argmin())  # argmin() returns index
# print("Max:", arr16.max(), "at index", arr16.argmax())

# # ======================
# # 7. Data Types
# # ======================

# # 7.1 Type conversion
# arr17 = np.array([1.2, 3.4, 5.6])
# print("\n7.1 Type conversion:")
# print("Original:", arr17.dtype)  # dtype shows data type
# print("As integers:", arr17.astype(int))  # astype() converts types

# # ======================
# # 8. Iteration
# # ======================

# # 8.1 Array iteration
# arr18 = np.array([1, 2, 3, 4])
# print("\n8.1 Iteration:")
# for num in arr18:
#     print(num, end=" ")
# print()

# # ======================
# # 9. Views vs Copies
# # ======================

# # 9.1 View vs copy
# arr19 = np.array([1, 2, 3, 4])
# view = arr19.view()  # View shares memory with original
# copy = arr19.copy()  # Copy creates independent duplicate
# copy[0] = 99
# print("\n9.1 View vs Copy:")
# print("Original:", arr19)
# print("View:", view)  # Reflects original changes
# print("Copy:", copy)  # Independent of original

# # ======================
# # 10. Array Manipulation
# # ======================

# # 10.1 Concatenation
# a20 = np.array([1, 2])
# b20 = np.array([3, 4])
# print("\n10.1 Concatenated:", np.concatenate((a20, b20)))  # Joins arrays

# # 10.2 Filtering
# arr21 = np.array([1, 2, 3, 4, 5])
# print("\n10.2 Filter >3:", arr21[arr21 > 3])  # Boolean indexing

# # 10.3 Where clause
# arr = np.array([10, 45, 60, 75, 30, 90])
# print("\n10.3 Where >50:", np.where(arr > 50))  # Returns indices
# print("Values >50:", arr[np.where(arr > 50)])

# # 10.4 Where with replacement
# result = np.where(arr > 50, arr, 0)  # Ternary operation
# print("Replace <=50 with 0:", result)

# # 10.5 Unique elements
# arr22 = np.array([1, 2, 2, 3, 3, 3])
# print("\n10.5 Unique:", np.unique(arr22))  # Returns sorted unique values

# # 10.6 Flattening
# arr23 = np.array([[1, 2], [3, 4]])
# print("\n10.6 Flattened:", arr23.flatten())  # Returns 1D copy
# print("Raveled:", arr23.ravel())  # Returns 1D view

# # 10.7 Transpose
# print("Transposed:\n", arr23.T)  # .T property transposes array

# # 10.8 Shuffling
# arr24 = np.array([1, 2, 3, 4, 5])
# print("\n10.8 Before shuffle:", arr24)
# np.random.shuffle(arr24)  # In-place operation
# print("After shuffle:", arr24)

# # ======================
# # 11. Insert/Delete
# # ======================

# # 11.1 Insert element
# arr25 = np.array([10, 20, 30, 40])
# print("\n11.1 Insert 100 at pos2:", np.insert(arr25, 2, 100))

# # 11.2 Delete element
# print("11.2 Delete first:", np.delete(arr25, 0))

# # 11.3 Add row/column
# original = np.array([[1,2],[3,4]])
# new_row = np.array([5,6])
# print("\n11.3 Add row:\n", np.vstack((original, new_row)))  # Vertical stack

# new_col = np.array([[5],[6]])
# print("Add column:\n", np.hstack((original, new_col)))  # Horizontal stack

# # ======================
# # 12. Matrix Operations
# # ======================

# # 12.1 Matrix multiplication
# mat = np.array([[1, 2], [3, 4]])
# print("\n12.1 Matrix product:\n", np.matmul(mat, mat))  # Also @ operator

# # 12.2 Vector operations
# v1 = np.array([1,2,3,4,5])
# v2 = np.array([6,7,8,9,10])
# print("\n12.2 Vector ops:")
# print("Addition:", v1 + v2)
# print("Element-wise mult:", v1 * v2)
# print("Dot product:", np.dot(v1, v2))

# # ======================
# # 13. File I/O
# # ======================

# # 13.1 Save arrays
# np.save('array1.npy', arr1)
# np.save('array2.npy', arr2)

# # 13.2 Load arrays
# print("\n13.2 Loading saved arrays:")
# print(np.load('array1.npy'))
# print(np.load('array2.npy'))