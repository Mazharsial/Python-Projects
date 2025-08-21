import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
add = a + b
mul = a * b
div = b / a
power = a ** 2

print("Add:\n",add)
print("Mul:\n",mul)
print("div:\n",div)
print("Power:\n",power)

# Universal functions (ufuncs)
sqrt = np.sqrt(a)
log = np.log(a + 1)
exp = np.exp(a)

print("Square root(a):\n",sqrt)
print("Log(a+1):\n",log)
print("Exp(a):\n",exp)

