class Atm:
  

  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()
    
  
  def menu(self):
    user_input = input("""
     Welcome to Atm
     press 1 to create pin
     prese 2 to credit Amount 
     press 3 to check Balance
     press 4 to withdraw Amount
     press 5 to change pin
     press 6 to exit
      """)
    
    if user_input == '1':
    #   create pin
        self.create_pin()
    elif user_input == '2':
    #   credit amount 
        self.credit_Amount()
    elif user_input == '3':
    #   check balance 
        self.check_Balance()
    elif user_input == '4':
    #   check withdraw
         self.Withdraw_Amount()
    elif user_input == '5':
    #   change pin
         self.Change_pin()
    else:
      print("Exiting the ATM. Goodbye!")
      exit()

  def create_pin(self):
     user_pin = input("Enter your pin to create")
     self.pin = user_pin
     print("Pin created successfully")  
     self.menu()

  def credit_Amount(self):
     check_pin = input("Enter your pin")  
     if check_pin == self.pin:
        Amount = int(input("Enter the Amount you want to credit"))
        self.balance = self.balance+Amount
        print("the balance is ", self.balance)
        self.menu()
     else:
        print("wrong pin")
        self.menu()

  def check_Balance(self):
     check_pin = input("Enter your pin") 
     if check_pin == self.pin:
        print("The balance is ",self.balance)
        self.menu()
     else:
        print("wrong pin")
        self.menu()
  def Withdraw_Amount(self):
       check_pin  = input("plzz enter your pin")
       if check_pin == self.pin:
          withdraw = int(input("Enter the amount you want to withdraw"))
          if withdraw <= self.balance:
             self.balance = self.balance - withdraw
             print("the balance is ",self.balance)
             self.menu()
       else:
          print("wrong pin")
          self.menu()

  def Change_pin(self):
      check_pin = input("Enter your pin")
      if check_pin == self.pin:
         new_pin = input("Enter new pin")
         self.pin = new_pin
         print("new pin create successfully")
         self.menu()
      else:
         print("wrong pin") 
         self.menu()


obj = Atm()  
    
