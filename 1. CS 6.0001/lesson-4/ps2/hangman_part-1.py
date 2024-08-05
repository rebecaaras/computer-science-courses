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

def is_in_secret_word(test_letter):
    if test_letter in secret_word:
        return True
    else:
        return False
    
def update_guessed_letters(test_letter):
  letter_position = 0
  
  for letter in secret_word:
    if test_letter == letter:
      guessed_letters[letter_position] = test_letter
    letter_position+=1

  return guessed_letters

def try_a_letter():
   
   test_letter = input('Try to guess a letter.').lower()
   if is_in_secret_word(test_letter):
      guessed_letters = update_guessed_letters(test_letter)
   else:
      num_guesses-=1
   return (guessed_letters, num_guesses)
  

wordlist = load_words()

def hangman(secret_word):
    guessed_letters = ['_' for i in len(secret_word)]
    #print('The word has {} letters.\n'.format(len(secret_word)))

    return

    
secret_word = choose_word(wordlist)
hangman(secret_word)