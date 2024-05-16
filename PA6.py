import random

def get_word_list(filename):
  """Given a string filename, return the contents of the file as a list of words."""
  words = {}
  words = open(filename).read().split()
  return words

def choose_word():
  """Chooses a random word from the word list"""
  return random.choice(get_word_list(r'C:\Users\banpr\Desktop\pritamBanpa6\pokemon.txt'))

def display_hangman(lives):
  """Prints different banner art depending on how many guesses the player has gotten wrong"""

  if lives == 6:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  ")
        print(" |  ")
        print(" |  ")
        print(" |  ")
        print(" +-----")
        print()
  elif lives == 5:
      print()
      print(" +--+")
      print(" |  |")
      print(" |  0")
      print(" |  ")
      print(" |  ")
      print(" |  ")
      print(" +-----")
      print()
  elif lives == 4:
      print()
      print(" +--+")
      print(" |  |")
      print(" |  0")
      print(" |  |")
      print(" |  ")
      print(" |  ")
      print(" +-----")
      print()
  elif lives == 3:
      print()
      print(" +--+")
      print(" |  |")
      print(" |  0")
      print(" |  |")
      print(" |   \\")
      print(" |  ")
      print(" +-----")
      print()
  elif lives == 2:
      print()
      print(" +--+")
      print(" |  |")
      print(" |  0")
      print(" |  |")
      print(" | / \\")
      print(" |  ")
      print(" +-----")
      print()
  elif lives == 1:
      print()
      print(" +--+")
      print(" |  |")
      print(" |  0")
      print(" |  |\\")
      print(" | / \\")
      print(" |  ")
      print(" +-----")
      print()
  elif lives == 0:
        print()
        print(" +--+")
        print(" |  |")
        print(" |  0")
        print(" | /|\\")
        print(" | / \\")
        print(" |  ")
        print(" +-----")
        print()
        print("I Win!")

def display_word(word, guessed):
  """Displays the partially guessed word"""
  displayed_word = ""

  for letter in word:
    if letter in guessed:
      displayed_word += letter + " "
    else:
      displayed_word += "- "
  print(displayed_word)

def guessLetterIV():
    """Validates the input of the 'play again' prompt, makes sure it is yes or no """

    val = input("Play again? (y/n): ").lower()
    while val != "y" and val != "n":
        val = input("Please enter 'y' or 'n': ")
    return val

def main():
  """Main game function, ! saves the word as a set to count several letters at once"""
  word = choose_word()
  word_letters = set(word)
  guessed_letters = set()
  lives = 6

  while len(word_letters) > 0 and lives > 0:
    display_hangman(lives)
    display_word(word, guessed_letters)
    print()
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
      print("You already guessed that letter!")
    elif guess in word_letters:
      guessed_letters.add(guess)
      word_letters.remove(guess)
    else:
      lives -= 1
      print("Incorrect guess!")

  display_hangman(lives)
  display_word(word, guessed_letters)
  if lives == 0:
    print("You lost! The word was", word)
  else:
    print("You won!")

  play_again = guessLetterIV()
  if play_again == 'y':
    main()


main()
