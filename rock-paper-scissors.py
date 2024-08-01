import random
import time
from colorama import init, Fore, Back, Style


# Initialize Colorama
init(autoreset=True)

# Game images
rock = '''
    _______  
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List to store the images
game_images = [rock, paper, scissors]

# Typewriter effect function

def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # for newline



# Function to get user input and validate it
def get_user_choice(player):
    while True:
        try:
            choice = int(input(f"{player}, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if choice in [0, 1, 2]:
                print(game_images[choice])
                return choice
            else:
                print("Invalid number, please choose 0, 1, or 2.")
        except ValueError:
            print("Invalid input, please enter a number.")

# Determine the winner based on choices
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a draw"
    elif (choice1 == 0 and choice2 == 2) or \
         (choice1 == 1 and choice2 == 0) or \
         (choice1 == 2 and choice2 == 1):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Main game loop
while True:    
    typewriter_effect("Do you have a playmate or want to play with the computer? Type '1' for playmate or '2' for computer: " )
    mode = input()
    if mode == '1':
        # Two-player mode
        print(Fore.RED + Back.GREEN + "Player 1's turn:")
        player1_choice = get_user_choice("Player 1")
        
        # Clear the screen or add separation (optional)
        print("\n" * 50)  # To create some space (to prevent Player 2 from seeing Player 1's choice)

        print(Fore.YELLOW + "Player 2's turn:")
        player2_choice = get_user_choice("Player 2")
        
        result = determine_winner(player1_choice, player2_choice)
        print(result)
    
    elif mode == '2':
        # Single-player mode
        player_choice = get_user_choice("Player")

        # Computer choice
        computer_choice = random.randint(0, 2)
        typewriter_effect(f"Computer chose:")
        print(game_images[computer_choice])

        # Determine winner
        if player_choice == computer_choice:
            print("It's a draw")
        elif (player_choice == 0 and computer_choice == 2) or \
             (player_choice == 1 and computer_choice == 0) or \
             (player_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose")
    
    else:
        print("Invalid input, please type '1' or '2'.")

    # Ask if the user wants to play again
    typewriter_effect("Do you want to play again? (yes/no): ")
    play_again = input().lower()
    if play_again != 'yes':
        break

typewriter_effect("Thanks for playing!")