
# Multiple classes inherit from the same parent class.

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.sound()
d.bark()
c.sound()
c.meow()
