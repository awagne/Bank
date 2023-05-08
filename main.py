import Bank


if __name__ == "__main__":

    print("Welcome!")
    bank = Bank.Bank([])
    print("What would you like to do?")
    choice = input("A) Create Account\nB) Delete Account\nC) Sign in\nD) Quit\n")

    while choice != "D":
        if choice == "A":
            bank.createAccount()
        elif choice == "B":
            num = input("Enter Account Number: ")
            bank.deleteAccount(num)
        elif choice == "C":
            name = input("Enter Account Holder: ")
            num = input("Enter Account Number: ")
            account = bank.getAccount(name, num)
            account.display()

            print("\nWhat would you like to do?")
            choice = input("A) Deposit\nB) Withdraw\nC) Quit\n")
            while choice != "C":
                if choice == "A":
                    print("Which account would you like to deposit in?")
                    accountType = input("Enter c for Checking\n Enter s for Savings\n")
                    value = input("How much would you like to deposit?")
                    if not account.deposit(value, accountType):
                        print("Invalid Deposit")

                elif choice == "B":
                    print("Which account would you like to withdraw from?")
                    accountType = input("Enter c for Checking\n Enter s for Savings\n")
                    value = input("How much would you like to withdraw?")
                    if not account.withdraw(value, accountType):
                        print("Invalid Withdrawl")
            
        print("\nWhat would you like to do?")
        choice = input("A) Create Account\nB) Delete Account\nC) Sign in\nD) Quit\n")