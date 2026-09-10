class Student :
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def display_details(self):
        print(f"Name:{self.name}\n Roll No :{self.rollno}\n Marks:{self.marks}")

student1 = Student("Prasanna",40596,99)
student1.display_details()
student2 = Student("Rohit",40597,95)
student2.display_details()
student3 = Student("Ramesh",40598,90)   
student3.display_details()