import unittest
from src.utils import load_words, choose_random_word

class TestUtils(unittest.TestCase):

    def test_load_words(self):
        # Assuming there's a words.txt file with some words for testing
        words = load_words('words.txt')
        self.assertIsInstance(words, list)
        self.assertGreater(len(words), 0)

    def test_choose_random_word(self):
        words = ['apple', 'banana', 'cherry']
        chosen_word = choose_random_word(words)
        self.assertIn(chosen_word, words)

if __name__ == '__main__':
    unittest.main()