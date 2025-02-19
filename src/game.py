class Game:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = ""
        self.guessed_letters = set()
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def start_game(self):
        self.secret_word = self.choose_random_word()
        self.guessed_letters.clear()
        self.attempts_left = self.max_attempts

    def choose_random_word(self):
        import random
        return random.choice(self.word_list)

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return False  # Letter has already been guessed
        self.guessed_letters.add(letter)
        if letter not in self.secret_word:
            self.attempts_left -= 1
        return True

    def check_win_condition(self):
        return all(letter in self.guessed_letters for letter in self.secret_word)

    def get_display_word(self):
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.secret_word)

    def is_game_over(self):
        return self.attempts_left <= 0 or self.check_win_condition()