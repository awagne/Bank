class Account:

    owner = ""
    type = ""
    checkings = 0
    savings = 0

    def __init__(self, owner, accountType):
        self.owner = owner
        self.type = accountType
        self.balance = 0

    def deposit(self, value, account):
        if(value >= 0):
            if(account == 'c'):
                self.balance += value
            if(account == 's'):
                self.savings += value
            return True
        return False

    def withdraw(self, value):
        if(value <= self.balance):
            self.balance -= value
            return True
        return False
    

        