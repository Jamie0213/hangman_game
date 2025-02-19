import unittest
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_start_game(self):
        self.game.start_game()
        self.assertIsNotNone(self.game.current_word)
        self.assertEqual(self.game.guessed_letters, [])
        self.assertEqual(self.game.remaining_attempts, self.game.max_attempts)

    def test_guess_letter_correct(self):
        self.game.start_game()
        letter = self.game.current_word[0]  # Assuming the first letter is correct
        self.game.guess_letter(letter)
        self.assertIn(letter, self.game.guessed_letters)
        self.assertEqual(self.game.remaining_attempts, self.game.max_attempts)

    def test_guess_letter_incorrect(self):
        self.game.start_game()
        letter = 'z'  # Assuming 'z' is not in the current word
        self.game.guess_letter(letter)
        self.assertIn(letter, self.game.guessed_letters)
        self.assertEqual(self.game.remaining_attempts, self.game.max_attempts - 1)

    def test_check_win_condition(self):
        self.game.start_game()
        self.game.guessed_letters = list(self.game.current_word)  # Simulate correct guesses
        self.assertTrue(self.game.check_win_condition())

    def test_check_loss_condition(self):
        self.game.start_game()
        self.game.remaining_attempts = 0  # Simulate loss
        self.assertFalse(self.game.check_win_condition())

if __name__ == '__main__':
    unittest.main()