# filepath: /hangman-game/hangman-game/src/main.py
from gui import HangmanGUI
from game import Game

def main():
    game = Game()
    gui = HangmanGUI(game)
    gui.setup_window()
    gui.start_game()

if __name__ == "__main__":
    main()