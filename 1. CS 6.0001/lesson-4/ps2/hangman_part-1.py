import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def display_dummy(guesses_used):
  dummy = ['-----\n    |\n', #0 guesses used
           '-----\n    |\n    O\n', #1 guess used
           '-----\n    |\n    O\n   /\n', #2 guesses used ...
           '-----\n    |\n    O\n   /|\n',
           '-----\n    |\n    O\n   /|\\\n',
           '-----\n    |\n    O\n   /|\\\n   /\n',
           '-----\n    |\n    X\n   /|\\\n   / \\\n\\\\\\\\\/////\n']
  print(dummy[guesses_used]+'\n')
  return None

def is_in_secret_word(test_letter, secret_word):
    if test_letter in secret_word:
        return True
    else:
        return False

def hangman(secret_word, num_guesses):

    guessed_letters = ['_' for i in range(len(secret_word))]
    display_dummy(6 - num_guesses)
    test_letter = input('Guess a letter. You have {} guesses.'.format(num_guesses)).lower()

    if is_in_secret_word(test_letter, secret_word) == True:
        letter_position = 0
        for letter in secret_word:
            if letter == test_letter:
                guessed_letters[letter_position] = test_letter
            else:
                continue
            letter_position+=1

        print('The letter {} is in the word!'.format(test_letter))
        print(' '.join(guessed_letters))
    else:
        num_guesses-=1
        print('The letter {} is not in the word. You have {} guesses.'.format(test_letter, num_guesses))
        print(' '.join(guessed_letters))

    return num_guesses

wordlist = load_words()
secret_word = choose_word(wordlist)
num_guesses = 6
while num_guesses > 0: 
    #display_dummy(6 - num_guesses)
    num_guesses = hangman(secret_word, num_guesses)

if num_guesses == 0:
    display_dummy(6)
    print('You died! The secret word was *{}*.'.format(secret_word))
