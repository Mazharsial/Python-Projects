# def my_function():
#   print("Hello from a function")

# my_function()


# # Passing Arguments
# def my_function(fname):#Parameter passing
#   print(fname + " Refsnes")

# my_function("Emil")#argument passing
# my_function("Tobias")
# my_function("Linus")

# def my_function(*kids):
#   print("The youngest child is " + kids[1])#Accessing items of tuple

# my_function("Emil", "Tobias", "Linus")#Tuple of arguments passing through function

# Passing arguments as key value pairs

# def my_function(child1, child2, child3):
#    print("The youngest child is ",child3)
#    print(f"then {child1} and then {child2}")

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Passing List as argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# # To let a function return a value, use the return statement:
# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))