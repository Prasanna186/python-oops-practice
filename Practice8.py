class Employee :
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    @staticmethod
    def is_valid_salary(salary):
        if salary < 0:
            return False
        return True
emp1 = Employee("Prasanna", 50000)
print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(-10000))