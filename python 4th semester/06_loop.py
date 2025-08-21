# While loop

# Exit the loop when i is 3:

# i = 0
# while i < 6:
#   print(i)
#   if i == 3:
#     break  # exit the loop right now
#   i += 1

# With the continue statement we can stop the current iteration, and continue with the next:
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue  #just skip this iteration and then continou
#   print(i)

# For Loop
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# # Looping through string
# for x in "banana": 
#   print(x)

# Break Statement
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# Loop with range
# Using the start parameter:

# for x in range(2, 6):
#   print(x)

# Using the start parameter,end paramenter and also increament:

# for x in range(2,6,2):
#   print(x)

# # Print all numbers from 0 to 5, and print a message when the loop has ended:

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# # Nested Loop
# # Print each adjective for every fruit:

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)



# Number of rows for the pyramid
# rows = 10
# # Loop through each row
# for i in range(1, rows + 1):
#     # Print spaces and stars for center alignment
#     print(' ' * (rows - i) + '*' * (2 * i - 1))


# # Number of rows for the triangle
# rows = 5
# # Loop to print each row
# for i in range(1, rows + 1):
#     # Print i number of asterisks (*) in each row
#     print('*' * i)



# # Number of rows for the triangle
# rows = 5
# # Loop through each row
# for i in range(1, rows + 1):
#     # Print i asterisks aligned to the right
#     print(' ' * (rows - i) + '*' * i)




# # Set the number of rows and columns
rows = 4
cols = 6

# Loop through each row
for i in range(rows):
    if i == 0 or i == rows - 1:
        # Print full row of stars for the top and bottom
        print('*' * cols)
    else:
        # Print star, spaces, then star for the middle rows
        print('*' + ' ' * (cols - 2) + '*')

