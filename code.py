import random

word_list =  ['Backpack', 'Hangman']


def get_word():
    word = random.choice(word_list)
    return word.upper()

