class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Welcome to our bank")

    def deposite_money(self, amount):
        self.balance += amount

    def widraw_money(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("widraw amount is", amount)
        else:
            print("The amount {0} you are withraw is less than your balance {1}".format(amount, self.balance))

    def check_balance(self):
        print("Hi {0} total amount available in bank is {1}".format(self.name, self.balance))


ob = Account("Govinda", 2000)
ob.deposite_money(1000)
ob.widraw_money(15000)
ob.check_balance()

