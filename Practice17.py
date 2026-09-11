class Employee :
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def display_details(self):
        print(f"Employee Name : {self.name}\nEmployee ID : {self.employee_id}\nSalary : {self.salary}")
class Department :
    def __init__(self,department_name,manager):
        self.department_name = department_name
        self.manager = manager
    def display_details(self):
        print(f"Department Name : {self.department_name}")
        print(f"Manager Name : {self.manager.name}")
        print(f"Manager Employee ID : {self.manager.employee_id}")
        print(f"Manager Salary : {self.manager.salary}")
class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size
    def display_details(self):
        super().display_details()
        print(f"Team Size : {self.team_size}")
manager1 = Manager("Prasanna", 101, 80000, 5)
department1 = Department("IT", manager1)
department1.display_details()

