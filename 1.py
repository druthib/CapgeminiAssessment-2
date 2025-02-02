class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def display(self):
        print(f'name:{self.name},id:{self.id},department:{self.department}')
emp=Employee('luffy','01','hr')
emp.display()