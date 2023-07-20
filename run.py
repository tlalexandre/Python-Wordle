# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore

print(Fore.CYAN+"Welcome to Python Wordle\n")
print(Fore.BLUE+"Press Enter to start")
print(Fore.GREEN+"The rules are simple: Guess the word on the screen in the less tries possible.\n Try to input differents letters and see if they exist in the word.\n If the letter exists in word but is misplaced it will turn"+(Fore.YELLOW+" YELLOW\n"))

print(Fore.GREEN+"If the letter doesn't exist in the word, it will turn" +
      (Fore.RED+" RED\n"))

print(Fore.GREEN+"Good Luck !")

secret = "point"
user = "pinte"


def split_string(word):
    letters = []
    for letter in word:
        letters.append(letter)

    print(f"{letters} for the word {word}\n")

    return letters


split_string(secret)
split_string(user)
