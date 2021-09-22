highscore = 0
lives_remaining = 5

import random
import sys
import time
zz = 0.01
z = 1
timing = 0.07

# for character in line:
#     sys.stdout.write(character)
#     sys.stdout.flush()
#     time.sleep(timing)

    #Difficulty
def difficulty():
    global lives_remaining
    lives_remaining = 0
    print("Select one of the following difficulties:")
    print ("1. Easy |  2. Hard  |  3. Nightmare  ")
    difficulty = str(input("Answer: "))
    if difficulty=="1":
        lives_remaining += 5
    elif difficulty=="2":
        lives_remaining += 3
    elif difficulty=="3":
        lives_remaining += 1
    else:
        print("Please input a number from 1 to 3.")
        difficulty()
    print()
    print("You have ", lives_remaining, " lives remaining.")


def letterboard():
    global highscore
    print("Your score is:", highscore)
letterboard()


def ending():
    time.sleep(z)
    print()
    print("You have remained with", lives_remaining," lives.")
    time.sleep(z)
    print("The game is over. Thank you for playing!")
    print()
    time.sleep(z)
    letterboard()
    sys.exit()



class main():
    global highscore
    import random
    def flag():
        print()
        print()
        print("Suddently ...")
        time.sleep(z)
        print()
        print("A wild Sheldon Cooper arrives and you hear:")
        time.sleep(z)
        print()
        line = "Sheldon Cooper: \"Welcome to my show! Fun with Flags!\""
        print()
        for character in line:
             sys.stdout.write(character)
             sys.stdout.flush()
             time.sleep(timing)
        time.sleep(z)
        time.sleep(z)
        time.sleep(z)
        print()
        time.sleep(z)
        print("\nWaiting for applause ...")
        print()
        time.sleep(z)
        time.sleep(z)
        time.sleep(z)
        print(".")
        print()
        time.sleep(z)
        print("..")
        print()
        time.sleep(z)
        print("...")
        print()
        time.sleep(z)
        print("....")
        print()
        time.sleep(z)
        print(".....")
        print()
        time.sleep(z)
        print("......")
        print()
        time.sleep(z)
        print(".......")
        print()
        time.sleep(z)
        print("........")
        print()
        time.sleep(z)
        time.sleep(z)
        time.sleep(z)
        time.sleep(z)
        line = "Sheldon Cooper: \"Forget it, I have a question for you:\""
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(timing)

        print()
        time.sleep(z)
        print()

            
        def romanian_flag():
            global lives_remaining
            global highscore
            print()
            print("What is the country coresponding to the flag?")
            print()
            print('   \033[2;30;44m   \033[0;0m'+'\033[2;30;43m   \033[0;0m'+'\033[2;30;41m   \033[0;0m')
            print()
            print("Select one of the following:")
            print ("1. Sri Lanka |  2. Romania  |  3. Uzbekistan")
            answer = input("Answer: ")
            if answer == "1":
                print("The answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "2":
                print("Your answer is correct.")
                highscore = highscore + 10
            elif answer == "3":
                print("Your answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("Please enter 1, 2 or 3.")
                romanian_flag()
            print("You have a remaining of", lives_remaining, "lives remaining.")
            letterboard()

        def france_flag():
            global lives_remaining
            global highscore
            print("What is the country coresponding to the flag?")
            print()
            print('   \033[2;30;44m   \033[0;0m'+'\033[2;30;47m   \033[0;0m'+'\033[2;30;41m   \033[0;0m')
            print()
            print("Select one of the following:")
            print ("1. France  |  2. Italy  |  3. Kamchatka")
            answer = input("Answer: ")
            if answer == "1":
                print("The answer is correct.")
                highscore += 10
            elif answer == "2":
                print("Your answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "3":
                print("Your answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("Please enter 1, 2 or 3.")
                france_flag()
            print("You have a remaining of", lives_remaining, "lives remaining.")
            letterboard()

        def italy_flag():
            global lives_remaining
            global highscore
            print("What is the country coresponding to the flag?")
            print()
            print('   \033[2;30;42m   \033[0;0m'+'\033[2;30;47m   \033[0;0m'+'\033[2;30;41m   \033[0;0m')
            print()
            print("Select one of the following:")
            print ("1. Kamchatka  |  2. Luxembourg  |  3. Italy")
            answer = input("Answer: ")
            if answer == "1":
                print("The answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "2":
                print("Your answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "3":
                print("Your answer is correct.")
                highscore = highscore + 10
            else: 
                print("Please enter 1, 2 or 3.")
                italy_flag()
            print("You have a remaining of", lives_remaining, "lives remaining.")
            letterboard()
            
            
        import random
        choice = random.randint(1,3)
        if (choice == 1):
            romanian_flag()
        if (choice == 2):
            france_flag()
        if (choice == 3):
            italy_flag()

    def riddle():
        global lives_remaining
        global highscore
        print()
        print()
        print("You see a door with a question mark on it")
        time.sleep(z)
        print()
        print("You see a you open the door to see..")
        time.sleep(z)
        print()
        print("The Riddler emerges from the far end of the room")
        time.sleep(z)
        print("He looks at you and smiles")
        time.sleep(z)
        print()
        time.sleep(z)
        time.sleep(z)
        time.sleep(z)
        line ="The Riddler: \"I've disposed of batman and now it's your turn\""
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(timing)
        print()
        time.sleep(z)
        line = "The Riddler: \"A good riddle reveals the asker. To solve it is to solve the mystery of the person posing it. Answer this question if you can\""
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(timing)

        def riddle_one():
            global lives_remaining
            global highscore
            print()
            time.sleep(z)
            line = "The Riddler: \"Can you solve this?:\""
            for character in line:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(timing)
            print()
            print("Lose me once i'll come back stronger, lose me twice i'll leave forever?")
            answer = input("Answer: ").lower().strip()
            correct_answer = "tooth"
            if answer == correct_answer:
                print("The answer is correct.")
                highscore = highscore + 10
            else:
                lives_remaining -= 1
                print("Unfortunately this is a wrong answer ")
            print("You have a remaining of", lives_remaining, "lives remaining.")
            letterboard()
            
        def riddle_two():
            global lives_remaining
            global highscore
            print()
            time.sleep(z)
            line = "The Riddler: \"This is a brain tickler:\""
            for character in line:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(timing)
            print()
            print("If you throw me out the \"window\"? " + "\n" + "You'll leave a greiving wife." + "\n" + "But leave me in the middle of the \"door\" and you might just save a life?")
            answer = input("Answer: (*hint it's a letter*) ").lower().strip()
            correct_answer = "n"
            if answer == correct_answer:
                print("The answer is correct.")
                highscore = highscore + 10
            else:
                print("Unfortunately this is a wrong answer ")
                lives_remaining -= 1
            print("You have a remaining of", lives_remaining, "lives remaining.")
            letterboard()
                    
        def riddle_three():
            global lives_remaining
            global highscore
            print()
            print()
            time.sleep(z)
            line = "The Riddler: \"This is a hard one:\""
            for character in line:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(timing)
            print()
            print("Name a fruit that you can take:" + "\n" + "1. the first letter and it becomes a crime?" "\n" + "2. the first two letters and becomes an animal" "\n" + "3. the first letter and last letter and it becomes a type of music?")
            answer = input("Answer: ").lower().strip()
            correct_answer = "grape"
            if answer == correct_answer:
                print("The answer is correct.")
                highscore = highscore + 10
            else:
                print("Unfortunately this is a wrong answer ")
                lives_remaining -= 1
            print("You have a remaining of", lives_remaining, "lives remaining.")
            letterboard()
 
        choice = random.randint(1,3)
        if (choice == 1):
            riddle_one()
        if (choice == 2):
            riddle_two()
        if (choice == 3):
            riddle_three()  

    def maths_boss():
        global lives_remaining
        global highscore
        print("The Crazy old cat lady")
        time.sleep(z)
        print("------------------------")
        time.sleep(z)
        print("you arrive at the electoral section it’s a bright and shiny full of neon light and TV screens"+"\n"+"you see the last PS5 on the top shelf but wait ......")
        time.sleep(z)
        print("A little old lady has just pick it up for herself")
        time.sleep(z)
        print("You have to have that PS5 you think of all they was to get it of her push her over and grab it "+"\n"+"no one would know")
        time.sleep(z)
        print("You decide do go over and ask for it the lad looks and you and say you can have it if you answer my math equation "+"\n"+
                "Your surprised but take the offer")
        time.sleep(z)
        print("The little old lady cackles and says \"I want to play a game?\" \"See if you can solve my equation\"")
        def equation_one():
            global lives_remaining
            global highscore
            print("What is the result of this equation?:")
            print("Come on any time today would be nice")                   
            print ("~~~~~~~~~~~~~~~") 
            print("|  7 * 2 - 2 =  |")
            print ("~~~~~~~~~~~~~~~")
            answer = input("what is your answer: → ")
            if answer == "12":
                print("You're a wizard.")
                highscore = highscore + 10
            if answer == "10":
                print("For a guy with a four digit IQ, I must have missed something.")
                lives_remaining -= 1
                print("the old lady goes on and on and about 17 cats you feel like your going to die: ", lives_remaining,"lives.")
                highscore = highscore - 7
            if answer == "9":
                print("i feel bad for you.")
                lives_remaining -= 1
                print("the old lady goes on and on and about her life way back in the 80s i know she was crazy you feel weaker: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("☠ This is how I win ☠")
                lives_remaining -= 1
                print("she slap you across the face she was a black belt: ", lives_remaining,"lives.")
                highscore = highscore - 7
            letterboard()
        def equation_two():
            global lives_remaining
            global highscore
            print("What two numbers add to make 24?")
            num1=int(input("enter first number: "))
            num2=int(input("enter second number: "))
            answer= num1 + num2
            print (num1,"plus",num2,"is equal",answer)
            if answer == 24:
                print("that's it you got it well done take it.")
                highscore = highscore + 10
            elif answer == 15:
                print("your so close but not close enough.")
                lives_remaining -= 1
                print("you will have to do better then that she the old lady hits you with her bag: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == 12:
                print("what was that.")
                lives_remaining -= 1
                print("the old lady shows you pictures of her grandchildren must of been for 2 hours: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("☠ HAHAHAHAHA not even close ☠")
                lives_remaining -= 1
                print("the old lady hits and then starts telling you about her time working as a teacher: ", lives_remaining,"lives.")
                highscore = highscore - 7
                letterboard()
        def equation_three():
            global lives_remaining
            global highscore
            print("The little old lady looks crazy but you really want that item "+"\n"+"I'm gonna make you an offer you can't refuse")
            print("~~~~~~~~~~~~~~~~")
            print("|  6 / 3 + 3 =  |")
            print("~~~~~~~~~~~~~~~~")
            answer = input("what is your answer: → ")
            if answer == "5":
                print("OMG you got it.")
                highscore = highscore + 10
            elif answer == "3":
                print("not good.")
                lives_remaining -= 1
                print("the old lady laughs at you you die a little in side: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "7":
                print("that was way off go back to school :).")
                lives_remaining -= 1
                print("you just walk away crying inside: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("☠ you going to be sleeping with the fishes ☠ ")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            letterboard()
        def equation_four():
            global lives_remaining
            global highscore
            print("What two numbers add up to make 50?")
            num1=int(input("enter first number: "))
            num2=int(input("enter second number: "))
            answer= num1 + num2
            print (num1,"plus",num2,"is equal",answer)
            if answer == 50:
                print("your right.")
                highscore = highscore + 10
            elif answer == 24:
                print("close but no cigar.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == 9:
                print("sorry but get lost.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("☠ you are the weakest link goodbye ☠")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            letterboard()

        old_lady = random.randint(1,4)
        if (old_lady == 1):
            equation_one()
        if (old_lady == 2):
            equation_two()
        if (old_lady == 3):
            equation_three()
        if (old_lady == 4):
            equation_four()

# trivia_boss was broken, so removed and redirected to ending, easily fixed if you have time after the course

    # def trivia_boss():
    #     def intro_trivia():
    #         global lives_remaining
    #         dialogue=input("Are you ready?").lower()
    #         if dialogue==("yes"):
    #             print("\n")
    #             print("Well well.....Lets get started then shawll we.")
    #             print("\n")
    #         elif dialogue==("no"):
    #             print("\n")
    #             print("I pitty the fool who tries to take on Mr T")
    #             print("\n")
    #         else:
    #             print("please enter yes or no")
    #             print("\n")
    #             intro_trivia()
    #     intro_trivia()
    #     global highscore
    #     print=("As you scramble thought the sea of people rushing around during the sale. A silhouette of a large figure is standing in front of you"+"\n"+"Suddenley the figure turns around and points a large  finger atyour direction and he says...")
    #     time.sleep(z)
    #     line="\"Mr T is my name and asking questions is my game!You look like you need help fool? But I can only halp you if you answer my questions\"\n"
    #     for character in line:
    #         sys.stdout.write(character)
    #         sys.stdout.flush()
    #         time.sleep(timing)
    #     time.sleep(z)
    #     #Question 1
    #     def question_one():
    #         global lives_remaining
    #         global highscore
    #         ans_one=input("What is a Chinese gooseberry also known as?\n a.Blueberyy\n b.Watermelon\n c.Kiwifruit\n d.Pitahaya\n Answer: ")
    #         if ans_one=="c" or ans_one=="Kiwifruit":
    #             print("Correct!")
    #             print("\n")
    #             highscore = highscore + 20
    #         else:
    #             print("I pitty the fool who is Incorrect!")
    #             print("\n")
    #             lives_remaining -= 1
    #             print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
    #             highscore = highscore - 6
    #             letterboard()
    #     #Quetion 2
    #     def question_two():
    #         global lives_remaining
    #         global highscore
    #         ans_two=input("What popular Disney animated movie is named after a French cuisine?\n a.Pineapple Express\n b.Ratatouille\n c.Milk\n d.The Children of the Corn\n Answer: ")
    #         if ans_two=="b" or ans_two=="Ratatouille":
    #             print("Correct!")
    #             print("\n")
    #             highscore = highscore + 16
    #         else:
    #             print("I pitty the fool who is Incorrect!")
    #             print("\n")
    #             lives_remaining -= 1
    #             print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
    #             highscore = highscore - 7
    #             letterboard()
    #     #Question 3
    #     def question_three():
    #         global lives_remaining
    #         global highscore
    #         ans_three=input("what comic series is The Condiment King appear in\n a.Flaming Carrot\n b.Batman\n c.Aque Teen Hunger Force\n d.Eye Scream\n Answer: ")
    #         if ans_three=="b" or ans_three=="Batman":
    #             print("Correct Fool!")
    #             print("\n")
    #             highscore = highscore + 14
    #         else:
    #             print("Incorrect Fool!")
    #             print("\n")
    #             lives_remaining -= 1
    #             print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
    #         highscore = highscore - 8
    #         letterboard()
    #     choice = random.randint(1,3)
    #     if (choice == 1):
    #         question_one()
    #     if (choice == 2):
    #         question_two()
    #     if (choice == 3):
    #         question_three()
    #     line="Mr T:\I pitty the fool who messes with you! all those jive turkeys beter watch out casue you aint playing around!"+"\n"+" Mr T looks at you, slowly he turn his head towards the cieleing and with his Frohawk looking amazing turns into a puff of smoke..nothing remains but the smell of cocobutter and a red feather on the ground."
    #     for character in line:
    #         sys.stdout.write(character)
    #         sys.stdout.flush()
    #         time.sleep(timing)

    def spelling_boss():
        global highscore
        print("Sphynx Comes alive")
        print("")
        print("Another Challenger, I hope your more resiliant than the last one.")
        print("")
        print("")
        print("One must risk everything in the pursuit of knowledge, ")
        print("If you can answer my questions wiseley,")
        print("You will have proven yourself worthy.")
        print("")
        print("")

        def school_class():
            global lives_remaining
            global highscore
            print("Fill in the blank.")
            print("... 5 minutes late to the lesson!")
            print ("1. You’re  |  2. Your  |  3. Yawr")
            answer = input("Answer: ")
            if answer == "1":
                print("The answer is correct.")
                highscore = highscore + 10
            elif answer == "2":
                print("Your answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "3":
                print("Your answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("Your answer is incorrect")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            

        def lex_luthor():
            global lives_remaining
            global highscore
            print("Fill in the blank.")
            print("Son of ....... vs Bat of Gotham!")
            print ("1. Kripton | 2. Crypton  | 3.Krypton  | 4. Cripton ")
            answer = input("Answer: ")
            if answer == "1":
                print("The answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "2":
                print("Your answer is incorrect.")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "3":
                print("Your answer is correct.")
                highscore = highscore + 10
            elif answer == "4":
                print("Your answer is incorrect")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("Your answer is incorrect")
                lives_remaining -= 1
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            letterboard()

        def brotherhood():
            global lives_remaining
            global highscore
            print("Fill in the blank.")
            print("We work in the dark, to serve the Light. We are ...")
            print ("1. Asassins  | 2. Assassins  | 3.Asassins  | 4. Asasins ")
            answer = input("Answer: ")
            if answer == "1":
                print("The answer is incorrect.")
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            elif answer == "2":
                print("Your answer is correct.")
                highscore = highscore + 10
                lives_remaining -= 1
            elif answer == "3":
                print("Your answer is incorrect.")
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
                lives_remaining -= 1
            elif answer == "4":
                print("Your answer is incorrect")
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
            else:
                print("Your answer is incorrect")
                print("You have lost one life. You have a remaining of: ", lives_remaining,"lives.")
                highscore = highscore - 7
                lives_remaining -= 1
            letterboard()

        test_of_sphyinx = random.randint(1,3)
        if (test_of_sphyinx == 1):
            school_class()
        if (test_of_sphyinx == 2):
            lex_luthor()
        if (test_of_sphyinx == 3):
            brotherhood()

    def secret_room():
        global highscore
        global lives_remaining
        time.sleep(z)
        print("You've entered in a secret area.")
        print()
        time.sleep(z)
        print("In the corner there is an old computer.")
        print()
        print("You can read on the screen:")
        print()
        time.sleep(z)
        line= "PASSWORD: "
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(timing)
        time.sleep(z)
        print()
        secret_answer = input("Your input: ")
        if secret_answer == "your_mind":
            highscore = highscore + 100
            print("You have a keen eye for easter eggs! Good job!")
            print("You've added 100 points to your highscore.")
            print("Your current highscore is ", highscore)
        else: 
            print("That is not correct, better luck next time!")
    



print()
print()
print("      ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   ")
print("     |                       | ")
print("                               ")
print("     |      Black Friday     | ")
print("              Madness          ")
print("     |   - Python Edition -  | ")
print("                               ")
print("     |                       | ")
print("      ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ")
time.sleep(z)
time.sleep(z)
time.sleep(z)
print()
print()
print("Remember: the password is your_mind")
time.sleep(z)
print()
time.sleep(z)
print()
time.sleep(z)
# difficulty()
print()
print("What room do you wish to begin with?")
time.sleep(z)
print()
print("Select one of the following:")
time.sleep(z)
def check_answer():
    print ("| 1. Fun with Flags |  2. Riddler  | 3. Crazy Cat Lady | 4. The Sphynx |")
    global_answer = input("Answer: ")
    if global_answer == "1":
        main.flag()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.riddle()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.maths_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.spelling_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.secret_room()
        print ("")
        print ("Well done. You have finished the game!")
        ending()
    elif global_answer == "2":
        main.riddle()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.maths_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.spelling_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.flag()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.secret_room()
        print ("")
        print ("Well done. You have finished the game!")
        ending()
    elif global_answer == "3":
        main.maths_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.spelling_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.flag()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.riddle()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.secret_room()
        print ("")
        print ("Well done. You have finished the game!")
        ending()
    elif global_answer == "4":
        main.spelling_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.flag()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.riddle()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.maths_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.secret_room()
        print ("")
        print ("Well done. You have finished the game!")
        ending()
    elif global_answer == "5":
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.spelling_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.flag()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.riddle()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with this room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.maths_boss()
        if lives_remaining <= 0:
            ending()
        print ("")
        print ("You are done with theis room!")
        print ("")
        print ("Good luck with the next one.")
        print ("")
        main.secret_room()
        print ("")
        print ("Well done. You have finished the game!")
    else:
        print("Please select one of the following:")
        check_answer()
        ending()
check_answer()


print("Your final score is:", highscore)


