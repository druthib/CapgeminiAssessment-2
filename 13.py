class Shape:
    def area(self):
        print("area of the shape")
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print(f"area:{self.side**2}")
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        print(f"area:{0.5*self.base*self.height}")
def myfunc(obj):
    obj.area()
t=Triangle(5,6)
s=Square(4)

myfunc(t)
myfunc(s)

