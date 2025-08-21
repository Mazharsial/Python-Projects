# 1. Basic addition using lambda
add = lambda a, b: a + b
print("Addition:", add(5, 3))  # Output: 8

# 2. Square of a number using lambda
square = lambda x: x * x
print("Square:", square(4))  # Output: 16

# 3. Check if a number is even
is_even = lambda x: x % 2 == 0
print("Is 10 even?", is_even(10))  # Output: True
print("Is 7 even?", is_even(7))    # Output: False

# 4. Sort a list of tuples by the second value using lambda
pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted pairs by second value:", sorted_pairs)  # Output: [(2, 1), (4, 2), (1, 3)]

# 5. Use lambda with map() to get squares
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print("Squares using map and lambda:", squares)  # Output: [1, 4, 9, 16]

# 6. Use lambda with filter() to get even numbers
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter and lambda:", evens)  # Output: [2, 4, 6]

# 7. Use lambda with reduce() to get product
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print("Product using reduce and lambda:", product)  # Output: 24
