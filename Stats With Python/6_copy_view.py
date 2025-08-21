import numpy as np
# Copy vs View
arr = np.array([1, 2, 3])
view = arr[:2]
copy = arr[:2].copy()
print("Original array:\n",arr)
print("View:\n",view)
print("Copy:\n",copy)

# Broadcasting
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
broadcasted_sum = a + b
print("Broadcasting sum:\n",broadcasted_sum)
