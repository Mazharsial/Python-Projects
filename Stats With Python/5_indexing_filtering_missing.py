import numpy as np

# Boolean indexing and filtering

x = np.array([10, 20, 30, 40, 50])
print("original array:\n",x)

# Boolean indexing
mask = x > 25
filtered = x[mask]
print("Filtered:\n",filtered)
# Direct
print(x[x % 20 == 0])

# Handling missing or invalid data

# With NaN
data = np.array([1, 2, np.nan, 4])
print("Data with Nan:\n",data)
# Check and remove
nan_mask = ~np.isnan(data)
print("nan mask:\n",nan_mask)
clean_data = data[nan_mask]
print("Clean data:\n",clean_data)

# Replace NaN with mean
data[np.isnan(data)] = np.nanmean(data)
print("Replaced Nan mean:\n",data)
