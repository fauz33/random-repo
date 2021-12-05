class Account:
    _ID = 0
    def __init__(self, name, balance):
        self.id = self._ID; self.__class__._ID += 1
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"

class DevAccount(Account):
    def getBalance(self):
        return f"{self.name}'s account. Balance: {self.balance}"

    def setBalance(self,balance):
        self.balance=balance

    def transferBalance(self,amount,otherAccount):
        self.balance = self.balance - amount
        otherAccount.balance = otherAccount.balance + amount


account1 = DevAccount("Ali",20)
account2 = DevAccount("Ahmad",30)

print(account1)
print(account2)

account1.transferBalance(10,account2)
print(account1)
print(account2)
