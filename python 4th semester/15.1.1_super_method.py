# The super() method in Python is used to call methods from a parent class. It is especially helpful when you're overriding a method in the child class but still want to use the parent’s version.

# Ineriting simple method
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call parent method
        print("Dog barks")

d = Dog()
d.speak()


# Inheriting constructor
class Person:
    def __init__(self, name):
        self.name = name
        print("Person name is:", name)

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)  # Call parent constructor
        self.roll = roll
        print("Student roll number is:", roll)

s = Student("Ali", 101)
