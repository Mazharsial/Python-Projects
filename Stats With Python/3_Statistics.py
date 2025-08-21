import numpy as np

data = np.array([1, 2, 3, 4, 5])

mean = np.mean(data)
median = np.median(data)
std = np.std(data)
var = np.var(data)
sum_ = np.sum(data)
min_ = np.min(data)
max_ = np.max(data)

print("Mean:\n",mean)
print("Median:\n",median)
print("standard deviation:\n",std)
print("Variance:\n",var)
print("Sum:\n",sum_)
print("Minimum:\n",min_)
print("Maximum:\n",max_)

# Axis-wise operations
matrix = np.array([[1, 2], [3, 4]])
row_sum = np.sum(matrix, axis=1) #row wise sum
col_mean = np.mean(matrix, axis=0) #column wise mean

print("Matrix:\n",matrix)
print("Row Sum:\n",row_sum)
print("Col mean:\n",col_mean)
