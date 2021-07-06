import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word\
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    Lives = 6

    while len(word_letters) > 0 and Lives > 0: 

        print('You have', Lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                Lives = Lives - 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print('You have already guessed this letter. Please try again.')
        else:
            print('Invalid character. Please try again.')
    if Lives == 0:
        print(f"You died!\nThe correct word was: {word}")
    else:
        print(f"You have guessed the word {word} correctly!")
    
hangman()