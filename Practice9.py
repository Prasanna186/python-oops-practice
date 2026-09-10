class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Employee Name : {self.name}\nSalary : {self.salary}")
class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language = programming_language
    def display_details(self):
        super().display_details()
        print(f"Programming Language : {self.programming_language}")
dev = Developer("Prasanna", 50000, "Python")
dev.display_details()
emp = Employee("Rohit", 60000)
emp.display_details()