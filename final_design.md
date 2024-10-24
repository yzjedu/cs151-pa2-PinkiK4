# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 
1. Import random into program
2. Create variable play_again and set it to an empty string
3. Create variable player1_losses and set it to 0
4. Create variable player2_losses and set it to 0
5. Create variable computer_losses and set it to 0
6. Output the game name and the game's goal

Name: game_over\
Parameters: num_sticks\
Return: num_sticks > 1

Name: player_choice\
Parameters: player, num_sticks\
Return: choice
   1. Create variable choice, convert it to an integer, and asks user whether they want to input 1, 2, or 3
   2. If choice is equal to 1 or 2 or 3 and choice is less than or equal to num_sticks, return choice
   9. Otherwise 
      1. Output that user input an invalid value
      2. Prompt user to input valid value
      3. Return choice

Name: computer_choice\
Parameters: None\
Return: choice  
   1. Create variable choice, and set it to choose a random integer between 1-3.
   11. Output how many sticks the computer chooses to take

Name: stick_game\
Parameters: num_sticks = 0\
Return: none
   1. Create variable play_again and ask user to input if they wanted to play
   2. Convert play_again variable to lowercase and strip it of white space
   3. While play_again is not 'y' or play_again is not 'n'
      1. Output that user input was invalid
      2. Create variable play_again and ask user to input if they wanted to play
   4. Convert variables player1_losses, player2_losses, and computer_losses to global variables
   5. While play_again is not 'n'
      1. Ask user how many sticks (between 10-100) are on the table
      2. Create variable num_sticks, set it to user's input, and convert it to an integer
      3. If num_sticks is less than 9 and num_sticks is greater than 101
         1. Break
      4. Otherwise
         1. Output that user input is invalid
         2. Prompt user to retry input
         3. Break
   6. Output the number of sticks in the game
   7. Set variable player equal to 1
   8. While function game_over is not true or play_again is not 'n'
      1. Output the number of sticks remaining
      2. If player is equal to 1
         1. Set variable choice to invoked function player_choice with arguments 'Player 1' and num_sticks
      3. Otherwise if player is equal to 2
         1. Set variable choice to invoked function player_choice with arguments 'Player 2 and num_sticks
      4. Otherwise
         1. Set variable choice to invoked function computer_choice
      5. Subtract values inputted in choice variable and subtract it from num_sticks variable
      6. If function game_over is true
         1. If player is equal to 1
            1. Output that player 1 has to choose the last stick and they lose
            2. Add 1 loss to variable player1_losses
         2. Otherwise if player is equal to 2
            1. Output that player 2 has to choose the last stick and they lose
            2. Add 1 loss to variable player2_losses
         3. Otherwise
            1. Output that computer has to choose the last stick and computer loses
            2. Add 1 loss to variable computer_losses
         4. Break
      7. If variable player is equal to 1
         1. Set the variable player to 2
      8. Otherwise if variable player is equal to 2
         1. Set the variable player to 'Computer'
      9. Otherwise
         1. Set the variable player to 1
   9. Output that the game is over and thank users for playing
   10. Output current loses
11. While play_again is not 'n':
    12. Invoke function stick_game