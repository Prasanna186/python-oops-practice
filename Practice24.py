#Shared class state
class Employee :
    employee_count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count
emp1 = Employee("Prasanna",70000)
emp2 = Employee("Rohit", 45000)
emp3 = Employee("Kabiraj",90000)
print(Employee.employee_count)
print(Employee.get_employee_count())
