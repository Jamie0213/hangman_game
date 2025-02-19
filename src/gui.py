class HangmanGUI:
    def __init__(self):
        self.window = None
        self.word_display = None
        self.message_label = None
        self.guess_entry = None

    def setup_window(self):
        import tkinter as tk
        
        self.window = tk.Tk()
        self.window.title("Hangman Game")
        
        self.word_display = tk.Label(self.window, text="", font=("Helvetica", 24))
        self.word_display.pack(pady=20)

        self.guess_entry = tk.Entry(self.window, font=("Helvetica", 18))
        self.guess_entry.pack(pady=10)

        self.message_label = tk.Label(self.window, text="", font=("Helvetica", 16))
        self.message_label.pack(pady=20)

        guess_button = tk.Button(self.window, text="Guess", command=self.handle_guess)
        guess_button.pack(pady=10)

    def update_display(self, current_word):
        self.word_display.config(text=current_word)

    def show_message(self, message):
        self.message_label.config(text=message)

    def handle_guess(self):
        # Logic to handle the guess will be implemented here
        pass

    def run(self):
        self.window.mainloop()