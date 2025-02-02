class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if quantity<=self.stock:
            print("available")
        else:
            print("unavailable")
p=Product("rice",2000,20)
p.check_availability(10)
p.check_availability(60)