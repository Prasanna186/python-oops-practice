#Multiple Inheritance and Method Resolution Order (MRO)
class Father :
    def skills(self):
        print("Father has skills in programming")
class Mother :
    def skills(self):
        print("Mother has skills in cooking")
        super().skills()
class Child(Mother,Father) :
    def skills(self):
        print("Child has skills in both programming and cooking")
        super().skills()
child = Child()
child.skills()
print(Child.__mro__)