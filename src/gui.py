class HangmanGUI:
    def __init__(self, game):
        self.game = game

    def setup_window(self):
        # CLI 환경에서는 별도의 GUI 창을 만들지 않습니다.
        pass

    def start_game(self):
        self.game.start_game()
        self.update_display()
        while not self.game.is_game_over():
            guess = input("알파벳 한 글자를 입력하세요: ").strip()
            if not guess:
                continue
            if not self.game.guess_letter(guess):
                print("이미 입력한 글자입니다.")
            self.update_display()
        if self.game.check_win_condition():
            print("축하합니다! 맞추셨습니다!")
        else:
            print("게임 오버! 정답은 '{}'였습니다.".format(self.game.secret_word))

    def update_display(self):
        current_word = self.game.get_display_word()
        # 글자 사이에 공백을 추가하여 출력
        print("현재 단어:", ' '.join(current_word))

    def run(self):
        self.start_game()