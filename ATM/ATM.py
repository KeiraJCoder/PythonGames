# balance = 1000
# pin = 1234

# def atm_function(pin_entered, amount):
#     global balance 
#     if pin_entered == pin:
#         print ("Access granted")
#         if amount <= balance:
#             print(f"You may withdraw that amount {amount}")
#             balance -= amount 
#             print ("Your new balance is {}. Thankyou for using this bank".format(balance))
#     elif amount > balance:
#         print("You don't have enough")
#     else:
#         print ("That was incorrect")

# atm_function(1234, 333)




def cash_machine(): #! overall function
    global attempts
    attempts = 0
#######################################################
    def pin_func(): #! function 1 - takes a pin input and checks if it is correct
        pin = input("Please enter your pin...\n")
        if pin == "1234":
            print("Pin accepted")
            balance_func() #! correct - next function
        else:
            print("Incorrect pin!")
            global attempts
            attempts += 1
            if attempts  >= 3:
                print("We have seized your card for security purposes...\nHave a nice day.")
            else:
                pin_func() #! incorrect - return to start of function
#######################################################
    def balance_func(): #! function 2 - 
        global balance, withdrawal
        balance = 5000
        withdrawal = input("How much money would you like to withdraw?\n")
        if int(withdrawal) <= balance:
            print("Accessing account...")
            withdraw_func() #! correct - next function
        else:
            print("Insufficient funds!")
            balance_func() 
            #! incorrect - return to start of function
#######################################################
    def withdraw_func(): #! function 3
        global balance, withdrawal
        new_balance = balance - int(withdrawal)
        print(f"Please take your money and don't forget your card.\nYou're remaining balance is {new_balance}")
#######################################################
    pin_func()
#######################################################
cash_machine()