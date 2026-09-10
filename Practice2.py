class Employee :
    def __init__(self, employee_name,employee_id,salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.salary = salary
    def display_details(self):
        print(f"Employee ID :{self.employee_id}\n Salary : {self.salary}")
    def increase_salary(self,percentage):
        self.salary += (self.salary * percentage / 100)
        print(f"Salary increased by {percentage}%")
        print(f"New Salary : {self.salary}")
emp1 = Employee("Prasanna", 101, 50000)
emp2 = Employee("Rohit", 102, 60000)
emp3 = Employee("Ramesh", 103, 45000)

emp1.increase_salary(10)


emp1.display_details()
emp2.display_details()
emp3.display_details()