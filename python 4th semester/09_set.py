set = {1,5,5,6,'A', True}

# Empty Set is:
# e=set() # Dont use s={} as empty set

# print(set)
print(set.add(99))
# print(set)
# print(set.__len__())
thisset = {"apple", "banana", "cherry"}

# print(len(thisset))


# print(set)




phone_no ={'Ali': 1234 , 'Sana':12345,'Ahmad':678}
# print(phone_no)


phone_no['Ali']=567

print(phone_no['Ali'])



#if conditions

# age = 18

# if age >= 18:
#     # print("You are eligible to vote.")
# else :
#     # print("You are not eligible to vote.")


#for loops

# fruits = ["apple", "banana", "cherry","mango","orange","pineapple"]

# for fruit in fruits:
#     if fruit=="cherry":
#         break
#     print(fruit)

# fruits = ["apple", "banana", "cherry", "mango", "orange", "pineapple"]

# # Loop through a slice of the list (from index 1 to 4)
# for fruit in fruits[1:5]:  
    # print(fruit)


# With range

# fruits = ["apple", "banana", "cherry", "mango", "orange", "pineapple"]

# # Using range to iterate over indices from 1 to 4 (inclusive)
# for i in range(1, 5):  
#     # print(fruits[i])  # Accessing elements using the index


#while
# count = 1

# while count <= 5:
#     print("Count:", count)
#     count += 1  # Increment count
# #with range
# num = 1

# while num <= 5:
#     if num == 3:
#         break  # Stops the loop when num is 3
#     print(num)
#     num += 1



# add(elem)	Adds an element to the set.
# remove(elem)	Removes an element from the set; raises KeyError if not found.
# discard(elem)	Removes an element if it exists; no error if it doesn't.
# pop()	Removes and returns an arbitrary element. Raises KeyError if empty.
# clear()	Removes all elements from the set.
# copy()	Returns a shallow copy of the set.


A = {1, 2, 3}
B = {3, 4, 5}

# print(A.union(B))                # {1, 2, 3, 4, 5}
# print(A.intersection(B))         # {3}
print(A.difference(B))           # {1, 2}
# print(A.symmetric_difference(B)) # {1, 2, 4, 5}
