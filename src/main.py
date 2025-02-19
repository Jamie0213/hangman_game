# filepath: /hangman-game/hangman-game/src/main.py
from gui import HangmanGUI
from game import Game

def main():
    word_list = ["python", "hangman", "challenge", "code"]  # 예시 단어 리스트
    game = Game(word_list)
    gui = HangmanGUI(game)
    gui.setup_window()
    gui.start_game()

if __name__ == "__main__":
    main()