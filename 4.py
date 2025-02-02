class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display_deets(self):
        print(f"name:{self.name},rollno:{self.rollno}")
student_list=[]
n=int(input("no of students"))
for i in range(n):
    name=input("name:")
    rollno=input("rollno:")
    s=Student(name,rollno)
    student_list.append(s)
for s in student_list:
    s.display_deets()

        
        