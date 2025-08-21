# # tuples are ordered(indexed) and unchangeable

# thistuple = ("apple", "banana", "cherry")
# # print(thistuple)

# # Accessing the tuples

# thistuple = ("apple", "banana", "cherry")
# # print(thistuple[1])

# # Negative indexing

# thistuple = ("apple", "banana", "cherry")
# # print(thistuple[-1])

# # Return the third, fourth, and fifth item:

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# # print(thistuple[2:5]) #5th not included

# # Convert the tuple into a list to be able to change it:as
# # we cant change a tuple 

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# # print(x)

# # Adding in a tuple/ also we can remove like this

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# # print(thistuple)

# Adding tuple with tuple

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# # Unpacking a tuple:

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# # Loop through tuple

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# # Through referring indexes

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])



# # Some Important Methods of Tuples
# # Simple and Important Tuple Methods in Python

# 1. count()
# t = (1, 2, 3, 2, 4)
# print("Count of 2:", t.count(2))  # Output: 2

# 2. index()
# t = (10, 20, 30, 20, 40)
# print("Index of 20:", t.index(20))  # Output: 1

# 3. len() - built-in function
# t = (5, 10, 15)
# print("Length of tuple:", len(t))  # Output: 3

# # 4. Tuple Packing and Unpacking
# # Packing
# t = (1, 2, 3)
# # Unpacking
# a, b, c = t
# print("Unpacked values:", a, b, c)  # Output: 1 2 3

# # 5. Tuple Concatenation (+)
# t1 = (1, 2)
# t2 = (3, 4)
# print("Concatenated tuple:", t1 + t2)  # Output: (1, 2, 3, 4)

# 6. Tuple Repetition (*)
# t = (1, 2)
# print("Repeated tuple:", t * 3)  # Output: (1, 2, 1, 2, 1, 2)

# # 7. in operator
# t = (1, 2, 3)
# print("Is 2 in tuple?", 2 in t)  # Output: True

# # 8. Iterating Through a Tuple
# t = (10, 20, 30)
# print("Iterating through tuple:")
# for item in t:
#     print(item)
