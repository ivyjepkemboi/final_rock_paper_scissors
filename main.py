from game_logic import play_game
from utils import typewriter_effect

if __name__ == "__main__":
    typewriter_effect("Welcome to Rock, Paper, Scissors!")
    play_game()
    typewriter_effect("Thanks for playing!")
