# Multiple Inheritance some real life scenarios
class Employee :
    def work(self):
        print("Employee Works")
class Developer(Employee):
    def work(self):
        print("Developer writes software")
        super().work()
class DataScientist(Employee):
    def work(self):
        print("Data Scientist analyzes data")
        super().work()
class MLEngineer(Developer,DataScientist):
    def work(self):
        print("ML Engineer builds ML Systems")
        super().work()
ml_engineer = MLEngineer()
ml_engineer.work()
print(MLEngineer.__mro__)