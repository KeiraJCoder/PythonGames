balance = 1000
pin = 1234

def atm_function(pin_entered, amount):
    global balance 
    if pin_entered == pin:
        print ("Access granted")
        if amount <= balance:
            print(f"You may withdraw that amount {amount}")
            balance -= amount 
            print ("Your new balance is {}. Thankyou for using this bank".format(balance))
    elif amount > balance:
        print("You don't have enough")
    else:
        print ("That was incorrect")

atm_function(1234, 333)
