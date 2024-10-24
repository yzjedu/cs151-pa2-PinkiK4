# Programmed by Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: October 23, 2024
# Programming Assignment: 02

# The purpose of this code was to run a stick game where
# two users and a computer remove sticks until the last stick is taken

# Initialize necessary variables
import random
play_again = ''
player1_losses = 0
player2_losses = 0
computer_losses = 0

# Output game name and the purpose of the code
print('Welcome to The Stick Game! \nThe goal of this game is to avoid being the person to take the last stick!\nHave fun!')

# Function to identify when game should end
def game_over(num_sticks):
    return num_sticks < 1

# Function for player's choice of sticks
def player_choice(player,num_sticks):
    choice = int(input(f"\n{player}, choose to remove 1, 2, or 3 sticks: "))
# Checks users input for validity and corrects user if they input an invalid input
    if choice == 1 or choice == 2 or choice == 3 and choice <= num_sticks:
        return choice
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')
        choice = int(input(f"{player}, choose to remove 1, 2, or 3 sticks: "))
        return choice

# Function for computer's random choice
def computer_choice():
    choice = random.randint(1, 3)
    print (f'Computer chose to take {choice} sticks.')
    return choice

# Main function for the stick game
def stick_game(num_sticks=0):
    play_again = input("Would you like to play? (y/n) ")
    play_again = play_again.lower().strip()
# Checks users input for error, outputs if there is an error to user, and prompts user to retry input
    while play_again != 'y' and play_again != 'n':
        print('Invalid option. Please choose y or n.')
        play_again = input("Would you like to play? (y/n) ")
    global player1_losses, player2_losses, computer_losses
# Asks user to input the number of sticks on the table until user choses to not continue playing
    while play_again != 'n':
        print ("How many sticks are on the table?")
        num_sticks = int((input()))
# Checks user input of number of sticks and if user inputs an invalid amount it prompts user to enter valid number
        if num_sticks > 9 and num_sticks < 101:
            break
        else:
            print("Sorry, that's not a valid number. Try again.")
            num_sticks = int(input())
            break

# Output the number of sticks at the beginning of the game
    print (f'There are {num_sticks} number of sticks to begin this game')
# Assign player variable to a value of 1 to begin the game
    player = 1
# While function game_over isn't true or variable play_again is not n, player 1, player 2, and the computer are
# asked to continue taking sticks
    while not game_over(num_sticks) or play_again != 'n':
        print (f"There are {num_sticks} sticks remaining.")
        if player == 1:
            choice = (player_choice('Player 1', num_sticks))
        elif player == 2:
            choice = (player_choice('Player 2', num_sticks))
        else:
            choice = (computer_choice())
# Removes the number of sticks based on the three choices
        num_sticks -= choice
# If function game_over is true, considers which player is present, outputs that the player lost, and assigns a loss
# to that player
        if game_over(num_sticks):
            if player == 1:
                print ('Player 1 has to take the last stick, so Player 1 loses!')
                player1_losses += 1
            elif player == 2:
                print ('Player 2 has to take the last stick, so Player 2 loses!')
                player2_losses += 1
            else:
                print ("Computer has to take the last stick, so Computers lose!")
                computer_losses += 1
            break
# Cycles players 1, 2, and 'Computer' throughout the game
        if player == 1:
            player = 2
        elif player == 2:
            player = 'Computer'
        else:
            player = 1
# Outputs that the game ended and thanks the players for playing.
    print ('Game over. Thank you for playing!')
# Outputs the current count of player losses
    print('\nCurrent Count of Losses:')
    print(
        f"Player 1 Losses: {player1_losses} losses\nPlayer 2 Losses: {player2_losses} losses\nComputer Losses: {computer_losses} losses")


# Continues to run main function stick_game until play_again is 'n'
while play_again != 'n':
    stick_game()


