class Bank():
    bank_name = "State Bank"
    branch = "Hyderabad"
    ifsc_code = "SBIN0001234"
    minimum_balance=1000
    def __init__(self,name,accno,pan,balance,phn):
        self.name=name
        self.accno=accno
        self.pan=pan
        self.balance=balance
        self.phn=phn
    def deposit(self,amount):
        if amount > 0:
                self.balance += amount
                print("successful deposit")
        else:
                print("Invalid deposit")
    def withdraw(self,money):
        if money<=0:
              print("not valid")
        elif(self.balance-money<Bank.minimum_balance) :   
                print("not vaild ")
        else:
              self.balance-=money
              print("balance:",self.balance)
    def display(self):
            print(self.name,self.accno,self.pan,self.phn,self.balance)
    @classmethod
    def change_minimum_balance(cls, new_balance):
            if new_balance > 0:
                cls.minimum_balance = new_balance
                print("Updated successfully")
            else:
                print("Invalid minimum balance")

c1 = Bank("Chandini",12345678,"ABC345678",2500,9490172811)
c2 = Bank("Madhuri", 23415689,"EFG654921",1800,7330824822)
c1.deposit(2000)
c1.withdraw(1500)
c1.display()


Bank.change_minimum_balance(2000)

c2.withdraw(1500)
c2.display()