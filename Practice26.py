#Student system
class Student :
    school = "Oxford IIT Concept School"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Student marks : {self.marks}")
        print(f"School Name : {self.school}")
    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school
    @staticmethod
    def is_passed(marks):
        if (marks >= 40) :
            return True
        else :
            return False
student1 = Student("Prasanna", 85)
student2 = Student("Rohit", 72)
student3 = Student("Kabiraj", 35)
Student.change_school("XYZ School")
student1.display()
student2.display()
student3.display()
Student.is_passed(85)
Student.is_passed(35)
