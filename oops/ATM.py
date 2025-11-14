class Atm:
    #contructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
                      Hello , how would you like to proceed?
                      1. Enter 1 to create pin
                      2. Enter 2 to deposit
                      3. Enter 3 to withdraw
                      4. Enter 4 to check balance
                      5. Enter 5 to exit
                                                

""")
        if user_input == "1":
            print("Create pin")
            self.create_pin()
        elif user_input == "2":
            print("deposit")
            self.deposit()
        elif user_input == "3":
            print("withdraw")
            self.withdraw()
        elif user_input == "4":
            print("Balance")
            self.check_balance()
        else:
            print("Byyy")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")
    
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
           amount = int(input("Enter the Amount")) 
           self.balance = self.balance+amount
           print("Deposit Successfull")
        else:
            print("invalid PIN")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount your want to withdraw"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("operation successful")
            else:
                print("insufficient funds")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")

            

sbi = Atm()
sbi.deposit()