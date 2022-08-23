import random
from words import word_list
from diagram import  display_hangman
# word_list = ["insert", "hangman", "words", "mango", "keyboard", "python", "list","software","sindhu","window","culture","mobile"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.lower()


def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already tried", guess, "!")
            elif guess not in word:
                print(guess, "isn't in the word :")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried ", guess, "!")
            elif guess != word:
                print(guess, " is not in that word :")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
            
        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("*Congratulatuon* You won!!")
    else:
        print("I'm sorry, you lose the game. The word was is " + word + ". good luck next time!")




# def display_hangman(tries):
#     stages = [  """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / \\
#                    -
#                    """,
#                    """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     /
#                    -
#                    """,
#                    """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |
#                    -
#                    """,
#                    """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|
#                    |      |
#                    |
#                    -
#                    """,
#                    """
#                    --------
#                    |      |
#                    |      O
#                    |      |
#                    |      |
#                    |
#                    -
#                    """,
#                    """
#                    --------
#                    |      |
#                    |      O
#                    |
#                    |
#                    |
#                    -
#                    """,
#                    """
#                    --------
#                    |      |
#                    |      
#                    |
#                    |
#                    |
#                    -
#                    """
#
def main():
    word=get_word(word_list)
    play(word)

    while input("play again...? (Y/N)").upper()=="Y":
        word=get_word(word_list)
        play(word)

main()