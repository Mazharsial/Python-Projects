# The join() function is used to join elements of a list (or any iterable) into a single string.

# 1. Join a list of strings with a space
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print("Joined with space:", sentence)  # Output: Hello world from Python

# 2. Join with a hyphen
items = ["2025", "06", "23"]
date = "-".join(items)
print("Joined with hyphen:", date)  # Output: 2025-06-23

# 3. Join characters in a string with a comma
chars = list("CODE")
joined_chars = ",".join(chars)
print("Joined characters:", joined_chars)  # Output: C,O,D,E

# 4. Join numbers converted to strings
numbers = [1, 2, 3, 4]
joined_numbers = " + ".join(str(num) for num in numbers)
print("Joined numbers:", joined_numbers)  # Output: 1 + 2 + 3 + 4

# 5. Join a tuple of strings
t = ("apple", "banana", "cherry")
joined_tuple = " | ".join(t)
print("Joined tuple:", joined_tuple)  # Output: apple | banana | cherry

# 6. Join with newline character
lines = ["Line1", "Line2", "Line3"]
multi_line = "\n".join(lines)
print("Joined with newlines:\n" + multi_line)

# 7. Join an empty list
empty_list = []
result = "-".join(empty_list)
print("Joining empty list:", result)  # Output: (empty string)
