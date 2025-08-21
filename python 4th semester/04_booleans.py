# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Following values will return true always

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# Example
# The following will return True:

# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])

# Following values will return false

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})