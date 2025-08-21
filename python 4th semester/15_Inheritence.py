# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


# Child Class inheriting parents init function
  #   class Student(Person):
  # def __init__(self, fname, lname):
  #   Person.__init__(self, fname, lname)

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # super function use to call methods from parent class.here it calling constructor


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year


x = Student("Mike", "Olsen", 2019)

x = Person("John", "Doe")
x.printname()


