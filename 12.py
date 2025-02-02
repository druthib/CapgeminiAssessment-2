class Payment:
    def process_payment(self):
        print("payment is being processed")
class CreditCardPayment(Payment):
    def process_payment(self):
        print("Payment is done through credit card")
class PaypalPayment(Payment):
    def process_payment(self):
        print("Payment is done through paypal")
class BitcoinPayment(Payment):
    def process_payment(self):
        print("Payment is done through bitcoin")
def myf(obj):
    obj.process_payment()
c=CreditCardPayment()
myf(c)
p=PaypalPayment()
myf(p)
b=BitcoinPayment()
myf(b)
