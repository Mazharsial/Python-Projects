
# One class inherits from a child class which is also a child of another class.

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def weep(self):
        print("Weeping")

p = Puppy()
p.eat()
p.bark()
p.weep()
