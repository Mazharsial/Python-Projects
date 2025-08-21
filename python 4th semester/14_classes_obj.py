class Person:
  def __init__(self, name, age):#__init__()function is constructor which is called when object is created  
    self.name = name
    self.age = age

p1 = Person("John", 36)# p1 is object created here

print(p1.name)
print(p1.age)

# The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):# self(we can use other name) always pass here as parameter for object in main function
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# With myfunction
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Person.myfunc(p1) # this is the another method for call and object is passing here as argument 