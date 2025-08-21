import numpy as np

# From list
arr = np.array([1, 2, 3])

print("Array from list:\n",arr)

# 2D array
matrix = np.array([[1, 2], [3, 4]])

print("2D array matrix:\n",matrix)

# Zeros, Ones, Identity
zeros = np.zeros((2, 3))
print("zeros:\n ",zeros)
ones = np.ones((3, 2))
print("ones:\n ",ones)
identity = np.eye(3)
print("identity:\n ",identity)

# Range and Linspace
arange = np.arange(0, 10, 2)
print("Array Range:\n ",arange)
linspace = np.linspace(0, 1, 5)
print("linspace:\n ",linspace)

# Random arrays

print("Random Arrays:\n")
rand_uniform = np.random.rand(2, 3)
print("Random uniform:\n ",rand_uniform)
rand_normal = np.random.randn(2, 3)
print("Random normal:\n ",rand_normal)
rand_int = np.random.randint(1, 10, (3, 3))
print("Random int:\n ",rand_int)


# Inspection And Indexing

import numpy as np
print("Inspection:\n")
print("Shape of Array:\n ",arr.shape)        # Shape of array
print("Data Type of array:\n",arr.dtype)        # Data type
print("Number of Dimensions:\n ",arr.ndim)         # Number of dimensions

# Indexing
print("Indexing:\n")
print("Element at row 0, col 1:\n",matrix[0, 1])     # Element at row 0, col 1
print("All rows, column 1:\n",matrix[:, 1])     # : means All rows, column 1

# Slicing
print("Slicing: \n")
print("From index 1 to end:\n",arr[1:])          # From index 1 to end


# Reshaping and stacking

reshaped = np.reshape(arr, (3, 1))
print("Reshaped array:\n ",reshaped)
# reshaped = arr.reshape(3, 1) #we can also use this method(Same result)

# Stacking
v_stack = np.vstack([arr, arr])
print("V stack:\n ",v_stack)
h_stack = np.hstack([arr, arr])
print("H stack:\n ",h_stack)
