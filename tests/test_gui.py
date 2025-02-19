import unittest
from src.gui import HangmanGUI

class TestHangmanGUI(unittest.TestCase):

    def setUp(self):
        self.gui = HangmanGUI()

    def test_setup_window(self):
        self.gui.setup_window()
        # Check if the window is set up correctly
        self.assertIsNotNone(self.gui.window)
        self.assertEqual(self.gui.window.title(), "Hangman Game")

    def test_update_display(self):
        self.gui.setup_window()
        self.gui.update_display("test", 3)
        # Check if the display updates correctly
        self.assertEqual(self.gui.word_display.get(), "test")
        self.assertEqual(self.gui.attempts_display.get(), "Attempts left: 3")

    def test_show_message(self):
        self.gui.setup_window()
        self.gui.show_message("Test message")
        # Check if the message is displayed correctly
        self.assertEqual(self.gui.message_label.cget("text"), "Test message")

if __name__ == '__main__':
    unittest.main()