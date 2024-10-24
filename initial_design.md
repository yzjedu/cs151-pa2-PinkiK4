# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully
1. Assign count to zero
2. Import random into program
3. While play_again is not "n":
   1. Ask user how many sticks (between 10-100) are on the table
   2. If user input is <10 and >100:
      1. Output "Invalid Input"
      2. Ask user how many sticks (between 10-100) are on the table
   3. Otherwise: Assign value of user input of number of sticks to total_sticks
      1. While total_sticks > count
         1. Ask Player 1 how many sticks between 1-3 that they would like to take
         2. Calculate total_sticks - playerone_input
         3. Output remaining total_sticks value
         4. Ask Player 2 how many sticks between 1-3 that they would like to take
         5. Calculate total number of sticks - playertwo_input
         6. Output remaining total_sticks value
         7. Have a random integer value of 1-3 be selected by computer and assign that value to playerthree_input
         8. Calculate total_sticks - playerthree_input
         9. Output remaining total_sticks value
      2. Ask user do they want to play again (y/n) and assign it to value play_again 2. While value is not ['y' or 'n']:
         1. Output 'Invalid Input, Please Input Valid Input'
         2. Ask user do they want to play again (y/n) and assign it to value play_again.
      
What I am not sure about the code is how to have the program determine which player caused the game to end and how to add player loses to their previous losses.