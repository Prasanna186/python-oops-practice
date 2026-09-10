class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls,data):
        name,salary = data.split("-")
        return cls(name,int(salary))

emp1 = Employee.from_string("Prasanna-50000")
print(emp1.name)
print(emp1.salary)