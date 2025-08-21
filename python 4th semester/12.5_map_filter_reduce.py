
# map() → Applies a function to every item in an iterable.

# filter() → Filters items based on a condition.

# reduce() → Reduces a list to a single value (e.g., sum or product).



# Importing reduce from functools
from functools import reduce

# ================================
# MAP FUNCTION
# ================================

# Example 1: Square each number in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print("Squares using map:", squared)  # Output: [1, 4, 9, 16, 25]

# Example 2: Convert strings to uppercase
words = ['hello', 'world']
upper_words = list(map(str.upper, words))
print("Uppercase words using map:", upper_words)  # Output: ['HELLO', 'WORLD']

# ================================
# FILTER FUNCTION
# ================================

# Example 1: Filter even numbers from a list
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter:", even_nums)  # Output: [2, 4, 6]

# Example 2: Filter words with more than 3 letters
words = ["hi", "hello", "cat", "python", "go"]
long_words = list(filter(lambda x: len(x) > 3, words))
print("Words longer than 3 letters:", long_words)  # Output: ['hello', 'python']

# ================================
# REDUCE FUNCTION
# ================================

# Example 1: Sum of all numbers
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", total)  # Output: 10

# Example 2: Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product using reduce:", product)  # Output: 24

# Example 3: Find maximum number
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum using reduce:", maximum)  # Output: 4
