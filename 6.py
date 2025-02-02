class Vehicle:
    def __init__(self,model,brand,year):
        self.model=model
        self.brand=brand
        self.year=year
    def display_vehicle_info(self):
        print(f"Vehile Information: model:{self.model},brand:{self.brand},year:{self.year}")
    def start_engine(self):
        print("engine start")
class Car(Vehicle):
    def __init__(self, model, brand, year,seat_capacity):
        super().__init__(model, brand, year)
        self.seat_capacity=seat_capacity
    def display_car_info(self):
        print(f"seat_capacity={self.seat_capacity}")
    def open_trunk(self):
        print("trunk is open")
class Bike(Vehicle):
     def __init__(self, model, brand, year,milage):
        super().__init__(model, brand, year)
        self.milage=milage
     def display_bike_info(self):
        print(f"milage={self.milage}")
     def open_fuel(self):
        print("fuel tank is open")
class ElectricCar(Car):
     def __init__(self, model, brand, year, seat_capacity,battery_capacity):
        super().__init__(model, brand, year, seat_capacity)
        self.battery_capacity=battery_capacity
     def display_electricCar_info(self):
        print(f"battery_capacity:{self.battery_capacity}")
     def charge_capacity(self):
        print(self.battery_capacity)
e=ElectricCar('civic','honda',2000,4,80)
e.display_vehicle_info()
e.start_engine()
e.display_car_info()
e.open_trunk()
e.display_electricCar_info()
e.charge_capacity()

b = Bike("Ninja 300", "Kawasaki", 2022, 35)
b.display_bike_info()     
b.open_fuel()             
