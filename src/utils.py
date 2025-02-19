def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
    return [word.strip() for word in words]

import random

def choose_random_word(word_list):
    return random.choice(word_list) if word_list else None