import random
from word import words
import string

def valid_word(words):
    word=random.choice(words)
    while '-' in words or ' ' in words:
        word=random.choice(words)
    return word

def Hangman():
    word= valid_word(words).upper()
    wordletters= set(word)
    used_letter = set()
    alphabet= set(string.ascii_uppercase)


    while len(wordletters)>0:
        print("Used Letters are:",' ' .join(used_letter))

        wordlist= [letter if letter in used_letter else '-' for letter in word]
        print("Current Word: ", ' '.join(wordlist))

        user_letter= input('Your Guess').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in wordletters:
                wordletters.remove(user_letter)
        elif user_letter in used_letter:
            print("Letter already used")
        else:
            print("invalid character")




Hangman()