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
            name = print("Enter Account Holder: ")
            num = input("Enter Account Number: ")
            account = bank.getAccount(name, num)

        print("What would you like to do?")
        choice = input("A) Create Account\nB) Delete Account\nC) Sign in\nD) Quit\n")