
# One child class inherits from more than one parent class.

class Father:
    def skills(self):
        print("Gardening, Programming -> from father")

class Mother:
    def skills_2(self):
        print("Cooking, Art  -> from mother")

class Child(Father, Mother):
    def more_skills(self):
        print("Playing Guitar  -> It's child")

c = Child()
c.skills()        # Output depends on Method Resolution Order (Father first)
c.skills_2()
c.more_skills()
