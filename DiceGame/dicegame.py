# Needed to create random numbers to simulate dice roll
import random

# Welcome message to output
print("Welcome to the roll the dice game! Let's roll with it!")
# Initialise player scores to 0
player1_score = 0
player2_score = 0

# Repeat everything in this block 10 times
for i in range(10):

	# Generate random numbers between 1 and 6 for each player.
	player1_value = random.randint(1, 6)
	player2_value = random.randint(1, 6)
	
	# Display the values
	print("Player 1 rolled: ", player1_value)
	    
	print("Player 2 rolled: ", player2_value)



# Selection: based on comparison of the values, take the appropriate path through the code.
	if player1_value > player2_value:
	    print("player 1 wins this round.")
	    player1_score = player1_score + 1  # This is how we increment a variable
	elif player2_value > player1_value:
	    print("player 2 wins this round")
	    player2_score = player2_score + 1
	else:
	    print("It's a draw")

	input("Press enter to continue.")  # Wait for user input to proceed.

print("#")