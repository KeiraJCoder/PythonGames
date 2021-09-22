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

# stretch

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