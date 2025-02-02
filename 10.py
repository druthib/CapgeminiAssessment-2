class Electronics:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"brand:{self.brand},price:{self.price}")
class MobileDevice(Electronics):
    def __init__(self,brand,price,battery):
        super().__init__(brand,price)
        self.battery=battery
    def display(self):
        super().display()
        print(f"battery:{self.battery}")
class SmartPhone(MobileDevice):
    def __init__(self, brand, price, battery,cam):
        super().__init__(brand, price, battery)
        self.cam=cam
    def display(self):
        super().display()
        print(f"cam:{self.cam}")
sm=SmartPhone("pixel",100000,2000,64)
sm.display()
        