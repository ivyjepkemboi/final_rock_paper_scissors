import random
from db_setup import session
from models import Player
from utils import game_images, get_user_choice, determine_winner, typewriter_effect
from colorama import init, Fore, Back

def get_or_create_player(name):
    player = session.query(Player).filter_by(name=name).first()
    if not player:
        player = Player(name=name)
        session.add(player)
        session.commit()
    return player

def update_score(player, won):
    if won:
        player.score += 1
    session.commit()

def play_game():
    while True:    
        typewriter_effect("Do you have a playmate or want to play with the computer? Type '1' for playmate or '2' for computer: " )
        mode = input()
        if mode == '1':
            player1_name = input("Enter Player 1's name: ")
            player2_name = input("Enter Player 2's name: ")

            player1 = get_or_create_player(player1_name)
            player2 = get_or_create_player(player2_name)

            print("Player 1's turn:")
            player1_choice = get_user_choice(player1_name)
            print("\n" * 50)

            print("Player 2's turn:")
            player2_choice = get_user_choice(player2_name)

            result = determine_winner(player1_choice, player2_choice)
            print(result)

            if result == "Player 1 wins!":
                update_score(player1, True)
            elif result == "Player 2 wins!":
                update_score(player2, True)
        
        elif mode == '2':
            player_name = input("Enter your name: ")
            player = get_or_create_player(player_name)

            player_choice = get_user_choice("Player")

            computer_choice = random.randint(0, 2)
            typewriter_effect(f"Computer chose:")
            print(game_images[computer_choice])

            if player_choice == computer_choice:
                print("It's a draw")
            elif (player_choice == 0 and computer_choice == 2) or \
                (player_choice == 1 and computer_choice == 0) or \
                (player_choice == 2 and computer_choice == 1):
                print("You win!")
                update_score(player, True)
            else:
                print("You lose")
        
        else:
            print(Fore.RED + "Invalid input, please type '1' or '2'.")

        typewriter_effect("Do you want to play again? (yes/no): ")
        play_again = input().lower()
        if play_again != 'yes':
            break
