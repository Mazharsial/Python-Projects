
# Combination of more than one type of inheritance (usually multiple + multilevel).

class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C:
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()
