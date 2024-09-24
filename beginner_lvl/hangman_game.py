import nltk
import random

# nltk.download('words') ----> if the word list from the library hasn't been downloaded yet


def letter_index(word, letter):
    return [i for i, l in enumerate(word) if l == letter]


def hangman_game():
    word_list = list(set(w.lower() for w in nltk.corpus.words.words()))
    word = random.choice(word_list)
    guess = ''
    wrong_guesses = 0
    for letter in word:
        guess += '_'
    print(guess)
    while guess != word and wrong_guesses <= 15:
        letter = input('Enter a letter: ')
        if letter in word:
            indexes = letter_index(word, letter)
            word_letters = list(guess)
            for number in indexes:
                word_letters[number] = letter
            guess = ''.join(word_letters)
            print(guess)
        else:
            wrong_guesses += 1

    if guess == word:
        print('Congratulations! You won!')
    else:
        print('Maybe next time...')

hangman_game()