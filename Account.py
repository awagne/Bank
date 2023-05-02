from random import random

class Account:

    owner = ""
    checkings = 0
    savings = 0
    accountNum = 0

    def __init__(self, owner):
        self.owner = owner
        self.checkings = 0
        self.savings = 0
        self.accountNum = int(random() * 100000000000000000 + 10000000)

    def getOwner(self):
        return self.owner
    
    def getCheckings(self):
        return self.checkings
    
    def getSavings(self):
        return self.savings
    
    def getNum(self):
        return self.accountNum

    def deposit(self, value, account):
        if(value >= 0):
            if(account == 'c'):
                self.checkings += value
            if(account == 's'):
                self.savings += value
            return True
        return False

    def withdraw(self, value):
        if(value <= self.balance):
            self.balance -= value
            return True
        return False
    
    def display(self):
        print("Account Holder: " + self.owner)
        print("Account Number: " + str(self.accountNum))
        print("Checkings Balance: " + str(self.checkings))
        print("Savings Balance: " + str(self.savings))
    

        