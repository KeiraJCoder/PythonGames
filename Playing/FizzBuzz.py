#challenge 1

password = input("Please choose a password: \n")

if len(password) < 8:
    print("ERROR... Password is too short... \nPassword must be at least 8 characters long. \n")
else:
    print(f"Your Password has been set to {password}")
    
 #challenge 2
 
num = 15
if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5.")
else:
    print("This number is not divisible by 3 or 5.")   

# challenge 3

num = 126

if num % 3 == 0 and num % 7 == 0:
    print ("Fizzbuzz") 
elif num % 7 == 0:
    print ("Buzz") 
elif num % 3 == 0:
    print ("Fizz")
else:
    print (num)

# challenge 3 stretch

num = int(input("Enter a number: \n"))
num = int(num)
score = 0
if (num % 7 == 0) and (num % 3 == 0):
    print(f"{num} is fizzbuzz +100 points!")
    score += 100
elif num % 3 == 0:
    print(f"{num} is fizz +5 points!")
    score += 5    
elif num % 7 == 0:
    print(f"{num} is buzz +10 points")
    score += 10
else:
    print(f"{num} is not fizz or buzz. you get no points")
print(f"You Scored: {score}at the end. Well done!")

#challenge 4
word = input("Please select a word: \n")
first_letter = word[0]
last_letter = word[-1]
if first_letter == last_letter:
    print("The first and last letters are the same.")
else:
    print("The first and last letters do not match.")
  
#   challenge 5  

time = 15
town_of_work = ("chester")
place_of_home = ("home")

if time >= (8):
    print (town_of_work)
elif time >= (16): 
    print (place_of_home)
    
# challenge 6

num1 = 15
num2 = 8

if (num1 + num2) % 2 == 0:
    print ("Success")
else:
    print ("Massive Fail")
