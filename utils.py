import time
from colorama import init, Fore, Back

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
    print()

# Function to get user input and validate it
def get_user_choice(player):
    while True:
        try:
            choice = int(input(Fore.BLUE + f"{player}, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if choice in [0, 1, 2]:
                print(Fore.YELLOW + game_images[choice])
                return choice
            else:
                print(Fore.RED + "Invalid number, please choose 0, 1, or 2.")
        except ValueError:
            print(Fore.RED + "Invalid input, please enter a number.")

# Determine the winner based on choices
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a draw"
    elif (choice1 == 0 and choice2 == 2) or \
         (choice1 == 1 and choice2 == 0) or \
         (choice1 == 2 and choice2 == 1):
        return Fore.GREEN + "Player 1 wins!"
    else:
        return Fore.GREEN + "Player 2 wins!"
