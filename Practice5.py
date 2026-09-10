class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value


emp1 = Employee("Prasanna", 50000)

print(emp1.salary)

emp1.salary = 60000
print(emp1.salary)

emp1.salary = -1000000
print(emp1.salary)