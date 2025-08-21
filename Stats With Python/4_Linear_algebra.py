import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

# Dot product
dot_product = np.dot(A, B)
print("Dot Product: \n",dot_product)

# Matrix inverse
inv = np.linalg.inv(A)
print("inverse:\n",inv)

# Transpose
transpose = A.T
print("Transpose:\n",transpose)

# Determinant
det = np.linalg.det(A)
print("Determinent: \n",det)

# Eigenvalues and Eigenvectors
eig_vals, eig_vecs = np.linalg.eig(A)
print("Eigen Values: \n",eig_vals)


# Random Sampling (important for Ml/Ds)
import numpy as np

data = np.array([1, 2, 3, 4, 5])
print("Data: \n",data)
# Random seed (reproducibility)
random_seed=np.random.seed(42)
print("Random Seed: \n",random_seed)

# Random sampling
samples = np.random.choice(data, size=3, replace=False)
print("Random sampling:\n",samples)
# Shuffle
shuffle_=np.random.shuffle(data)
print("Shuffle:\n",shuffle_)
