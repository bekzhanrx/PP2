class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money > self.balance:
            print("You do not have enough money in your account!")
        else:
            self.balance -= money


x = BankAccount('Bekzhan', 120000)
print(x.balance)
print(x.owner)
x.deposit(124000)
print(x.balance)
x.withdraw(240000)
print(x.balance)
x.withdraw(5000)
