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

listAccount = []
listAccount.append(Account("Mohd",10))
listAccount.append(Account("Fauzi",15))
listAccount.append(Account("Jamaluddin",20))

for i in listAccount:
    print(i)
