"""
This is a simple SNAKE, WATER, GUN game developed by Aarya Bhusal. SNAKE, WATER, GUN is a classic game just like Rock, Paper, Scissors. The rules are simple. Two players plays the game (Here it's gonna be user and computer). If both chooses the same thing the game is drawn. Snake wins over Water, Water wins over Gun and Gun wins over Snake.
"""

# Import the random module
import random

# Create a list containing the elements of the list.
game_elements = ["snake", "water", "gun"]

# Create a function with game logic
def play(computer_choice):
    # Take the choice of the user as input
    user_choice = input("Enter SNAKE, WATER OR GUN : ").lower().strip()
    # Check if user has given only valid input
    if not (user_choice in game_elements):
        # If the user's input is unvalid take the input agian.
        print("Invalid Input! Try agian.")
        return play(computer_choice)
    else:
        # Write the main logic of the game
        if user_choice == computer_choice:
            return "Drawn"
        elif user_choice == "snake" and computer_choice == "water":
            return "Won"
        elif user_choice == "snake" and computer_choice == "gun":
            return "Lost"
        elif user_choice == "gun" and computer_choice == "water":
            return "Lost"
        elif user_choice == "gun" and computer_choice == "snake":
            return "Won"
        elif user_choice == "water" and computer_choice == "snake":
            return "Lost"
        elif user_choice == "water" and computer_choice == "gun":
            return "Won"
        
# Create a function to take computer's choice
def computer_choice():
    random_index = random.randint(0, 2)
    choice = game_elements[random_index]
    return choice

# Create a function to find if user wants to play agian.
def replay_func():
    replay = input("Do you want to play the game agian? [y/n] : ").lower()
    if "n" == replay:
        return False
    elif "y" == replay:
        return True
    else :
        print("Invalid input.")
        return replay_func()

# Run a loop so that user can continue playing
while True:
    comp_choice = computer_choice()
    player_status = play(comp_choice)
    print(f"The game is {player_status}! Computer choose {comp_choice}.")
    replay_status = replay_func()
    if not replay_status:
        break
    else:
        pass