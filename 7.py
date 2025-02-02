class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person_details(self):
        print(f"name:{self.name},age:{self.age}")
class Employee(Person):
    def __init__(self, name, age,emp_id):
        super().__init__(name, age)
        self.emp_id=emp_id
    def employee_details(self):
        print(f"name:{self.name},age:{self.age},emp_id:{self.emp_id}")
class Manager(Employee):
    def __init__(self, name, age, emp_id,department):
        super().__init__(name, age, emp_id)
        self.department=department
    def manager_deets(self):
        print(f"name:{self.name},age:{self.age},emp_id:{self.emp_id},department:{self.department}")
    def aprove_leave(self,employee):
        print(f"{self.name} approved leave request of {employee.name}")
person=Person('luffy',20)
employee=Employee("zoro",25,123)
manager=Manager("shanks",30,1,"hr")
person.person_details()
employee.employee_details()
manager.manager_deets()
manager.aprove_leave(employee)

        
        