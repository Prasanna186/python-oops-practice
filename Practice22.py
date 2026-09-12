class Employee :
    def __init__(self,name):
        self.name = name
        print("Employee initialized")
class Developer(Employee):
    def __init__(self,name):
        print("Developer Initialized")
        super().__init__(name)
class DataScientist(Employee):
    def __init__(self,name):
        print("Data Scientist Initialized")
        super().__init__(name)
class MLEngineer(Developer, DataScientist):
    def __init__(self,name):
        print("ML Engineer Initialized")
        super().__init__(name)
ml = MLEngineer("Prasanna Chowdary")
print(ml.name)
print(MLEngineer.__mro__)
