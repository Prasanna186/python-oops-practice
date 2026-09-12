# Class variables and instance variables
class Employee :
    company = "Deloitee"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
emp1 = Employee("Prasanna", 70000)
emp2 = Employee("Kabiraj", 80000)
print(emp1.name)
print(emp2.name)
print(emp1.company)
print(emp2.company)
Employee.company = "Google"
print(emp1.company)
print(emp2.company)
emp1.company = "Microsoft"
print(emp1.company)
print(emp2.company)
