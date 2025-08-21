# List

# list1 = [1,2,3]
# list1[1]=20
# print(list1)

# List type
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))


# list2 = [6,9.5,'m']
# print(list2*5)

# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)


# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A

B = A[:]
B

# Variable B references a new copy or clone of the original list

# Now if you change A, B will not change
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

# Membership

# list3 =[2,3,5,[6,7,8],9,10]
# print(list3[3])


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members


# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# checking if item present in list or not
thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
  # print("Yes, 'apple' is in the fruits list")

# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
# print(thislist)
# changing multiple values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
# print(thislist)

# To insert at the specific position
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
# print(thislist)

# To append or add at the end

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
# print(thislist)

# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
# print(thislist)

# The remove() method removes the specified item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
# print(thislist)

# Pop or remove in list

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
# print(thislist)

# Looping a List

thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# Print all items by referring to their index number:

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# Print all items, using a while loop to go through all the index numbers

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# # Making a new list on the base of any letter(here a)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

# print(newlist)

# newlist create by short method 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)
# # With range and condition
# newlist = [x for x in range(10) if x < 5]
# newlist = [x.upper() for x in fruits]
# # newlist = ['hello' for x in fruits]

# # condition can be in expression
# newlist = [x if x != "banana" else "orange" for x in fruits]

# # Sort the list numerically:(by default ascending)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# # Sort the list descending:

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# # Append list2 into list1:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)


# # Use the extend() method to add list2 at the end of list1:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)


# # List Methods

# # append()	Adds an element at the end of the list
# # clear()	Removes all the elements from the list
# # copy()	Returns a copy of the list
# # count()	Returns the number of elements with the specified value
# # extend()	Add the elements of a list (or any iterable), to the end of the current list
# # index()	Returns the index of the first element with the specified value
# # insert()	Adds an element at the specified position
# # pop()	Removes the element at the specified position
# # remove()	Removes the item with the specified value
# # reverse()	Reverses the order of the list
# # sort()	Sorts the list