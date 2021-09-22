print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) : ')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is a group of crows called? ')
    if answer.lower()=='murder':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: What country was Brie cheese originally from? ')
    if answer.lower()=='france':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What did the Romans call Scotland? ')
    if answer.lower()=='caledonia':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')