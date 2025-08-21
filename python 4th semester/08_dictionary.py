# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(thisdict)
# print(thisdict["brand"])


# Empty Dictionary is:
# dict_1={}

# # we can access just keys from the below method
# x = thisdict.keys()
# print(x)

# # we can access just values from the below method

# x = thisdict.values()
# print(x)

# x = thisdict.items()
# print(x)

# # Adding a new key value pair in a dictionary

# thisdict["color"] = "white"
# print(thisdict) #after the change

# # Checking if value exists

# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


# # Updating through the method
# thisdict.update({"year": 2020})

# # Getting just keys
# for x in thisdict.keys():
#   print(x)

# # Getting keys and values both
# for x, y in thisdict.items():
#   print(x, y)


# # Nested dictionaries
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}

print(myfamily)

#  Adding dictionaries
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }






# Some important dictionary methods

# Important Python Dictionary Methods

# 1. get(key, default)
my_dict = {"name": "Ali"}
print(my_dict.get("age", 20))     # Output: 20


# # Note: Important difference
# print(my_dict.get("name2"))       #it will return the none
# print(my_dict["name2"])   #it will return error

# # 2. keys()
# my_dict = {"a": 1, "b": 2}
# print(my_dict.keys())              # Output: dict_keys(['a', 'b'])

# # 3. values()
# print(my_dict.values())           # Output: dict_values([1, 2])

# # 4. items()
# print(my_dict.items())            # Output: dict_items([('a', 1), ('b', 2)])

# # 5. update(other_dict)
# d1 = {"a": 1}
# d2 = {"b": 2}
# d1.update(d2)
# print(d1)                         # Output: {'a': 1, 'b': 2}

# # 6. pop(key, default)
# my_dict = {"a": 1, "b": 2}
# print(my_dict.pop("a"))           # Output: 1
# print(my_dict)                    # Output: {'b': 2}

# # 7. popitem()
# my_dict = {"x": 10, "y": 20}
# print(my_dict.popitem())          # Output: ('y', 20) or ('x', 10) depending on Python version

# # 8. clear()
# my_dict = {"a": 1}
# my_dict.clear()
# print(my_dict)                    # Output: {}

# # 9. setdefault(key, default)
# my_dict = {"x": 5}
# print(my_dict.setdefault("x", 0))   # Output: 5
# print(my_dict.setdefault("y", 10))  # Output: 10
# print(my_dict)                       # Output: {'x': 5, 'y': 10}
