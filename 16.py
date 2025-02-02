from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def calculate_area(self,len,bre):
        print(f"area:{len*bre}")
class Circle(Shape):
    def calculate_area(self,radius):
        print(f"area:{3.14*radius*radius}")
c=Circle()
c.calculate_area(2)
r=Rectangle()
r.calculate_area(1,2)