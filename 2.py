class BankAccount:
    def __init__(self,totalbalance,depositammount,withdrawamount):
        self.totalbalance=totalbalance
        self.depositammount=depositammount
        self.withdrawammount=withdrawamount
    def deposit(self):
        if self.depositammount>0:
            print(f"{self.depositammount} has been deposited")
            self.totalbalance=self.totalbalance+self.depositammount
            print(f"total balance:{self.totalbalance}")
        else:
            print("Ammount should be positive")
    def withdraw(self):
        if self.totalbalance < self.withdrawammount:
            print("insufficient balance. Cant be withdrawn")
        else:
            print(f"{self.withdrawammount} has been withdrawn.")
            self.totalbalance=self.totalbalance-self.withdrawammount
            print(f"total balance:{self.totalbalance}")
b=BankAccount(1000,100,900)
b.deposit()
b.withdraw()