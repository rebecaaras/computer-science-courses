# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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

def display_dummy(guesses):
  dummy = ['-----\n    |\n', #0 guesses used
           '-----\n    |\n    O\n', #1 guess
           '-----\n    |\n    O\n   /\n', #2
           '-----\n    |\n    O\n   /|\n', #3
           '-----\n    |\n    O\n   /|\\\n', #4
           '-----\n    |\n    O\n   /|\\\n   /\n', #5
           '-----\n    |\n    X\n   /|\\\n   / \\\n\\\\\\\\\/////\n'] #6

  print(dummy[guesses])
  return None

def counts_guesses(num_guesses = 6):
    guesses_used = 0
    
    print('You have {} guesses.')
    


wordlist = load_words()

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('The word has {} letters.\n'.format(len(secret_word)) + '_ '*len(secret_word))

    return

    
secret_word = choose_word(wordlist)
hangman(secret_word)