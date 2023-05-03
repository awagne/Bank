import Account

class Bank:

    accounts = []

    def __init__(self, accounts):
        self.accounts = accounts

    def createAccount(self):
        owner = input("Enter Account Name: ")
        account = Account.Account(owner)
        self.accounts.append(account)
        account.display()

    def deleteAccount(self, accountNum):
        for account in self.accounts:
            if(account.getNum() == accountNum):
                self.accounts.remove(account)

    def getAccount(self,name, accountNum):
        for account in self.accounts:
            if(account.getOwner() == name and account.getNum() == int(accountNum)):
                return account
            
        return None

    def display(self):
        for account in self.accounts:
            account.display()
            print("")