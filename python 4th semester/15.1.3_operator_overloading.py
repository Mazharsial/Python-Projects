# 1. Operator Overloading
# In Python, you can change the meaning of operators (+, *, >, etc.) for your custom classes by overloading them using special methods.


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)  # Calls b1.__add__(b2)