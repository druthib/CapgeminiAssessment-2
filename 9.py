class Car:
    def move(self):
       print("car is moving")

class Airplane:
    def move(self):
        print( "airplane is flying") 

class FlyingCar(Car, Airplane):
    def move(self):
        super().move()
        Airplane.move(self)
    
flying_car = FlyingCar()
flying_car.move()
