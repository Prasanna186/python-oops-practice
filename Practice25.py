class Employee :
    company = "Deloitte"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Employee name : {self.name}")
        print(f"salary : {self.salary}")
        print(f"Company name : {Employee.company}")
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        
    @staticmethod
    def is_valid_salary(salary):
        if(salary > 0):
            return True
        else :
            return False
emp1 = Employee("Prasanna", 80000)
emp2 = Employee("Kabiraj", 90000)
Employee.change_company("Google")
emp1.display_details()
emp2.display_details()
print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(-1000))