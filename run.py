# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from IPython.display import clear_output
import os
from colorama import Fore, Back, init
import requests
init(autoreset=True)

BG = Back.LIGHTGREEN_EX
BR = Back.RED
FC = Fore.CYAN
BY = Back.YELLOW
FW = Fore.WHITE
BM = Back.MAGENTA
ENDC = Back.RESET


def intro_display():
    print(FC+"Welcome to Python Wordle\n")
    print(FC+"Press Enter to start")
    print(FC+"The rules are simple: Guess the Wordle in 6 tries.\n Each guess must be a 5-letter word.\n Try to input differents letters and see if they exist in the word.\n ")
    print(FW+"If the letter does exist in the word and in the correct spot,\n it will display in "+(BG+"GREEN\n"))
    print("If the letter exists in word but is misplaced it will turn "+(BY+"YELLOW\n"))
    print(FW+"If the letter doesn't exist in the word, it will turn " +
          (BR+"RED\n"))

    print(FW+"Good Luck !")


def ask_word_length():
    while True:
        try:
            length = int(
                input("Enter the desired word length(min:1 max:10): "))
            if length < 1 or length > 10:
                print("Please enter a length between 1 and 10.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                word_string = data[0]
                return word_string
            else:
                print("Invalid response format or empty list.")
                return None
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None


def user_word():
    user_input = input("Enter your word: ").upper()
    return user_input


def split_string(word):
    letters = []
    for letter in word:
        letters.append(letter)
    return letters


def check_length(user_letters, word_length):
    if len(user_letters) != word_length:
        print(f"You can only enter up to {word_length} letters.")
        return False
    return True


def check_real_word(user):
    try:
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{user}")

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                print(f"The word '{user}' exists in the dictionary.")
                return True
            else:
                print(f"The word '{user}' does not exist in the dictionary.")
                return False
        else:
            print(f"The word '{user}' does not exist in the dictionary.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return False


def victory(guess, secret):
    print(BM +
          f"Well Play ! You guessed in only {guess} times to find the word: {secret}")


wrong_letters = set()


def compare_letters(user_letters, secret_letters, wrong_letters):
    secret_letters = list(secret_letters)
    user_letters = list(user_letters)
    correct_positions = []
    misplaced_positions = []
    wrong_positions = []
    user_counts = {}
    secret_counts = {}

    for letter in secret_letters:
        secret_counts[letter] = secret_counts.get(letter, 0)+1

    for letter in user_letters:
        user_counts[letter] = user_counts.get(letter, 0)+1

    for i, letter in enumerate(user_letters):
        if letter == secret_letters[i]:
            correct_positions.append(i)

    for i, letter in enumerate(user_letters):
        if letter in secret_letters and i not in correct_positions:
            misplaced_positions.append(i)

    for i, letter in enumerate(user_letters):
        if letter not in secret_letters or user_counts[letter] > secret_counts[letter]:
            wrong_positions.append(i)
            wrong_letters.add(letter)

    for i, letter in enumerate(user_letters):
        if i in correct_positions:
            print(BG+f"{letter}")
        elif i in misplaced_positions and i not in wrong_positions:
            print(BY+f"{letter}")
        elif i in wrong_positions:
            print(BR+f"{letter}")
    print("\n")
    print(BR+f"Here's the letters you tried and were wrong: {wrong_letters}")
    print("\n")
    return wrong_letters


def play_again():
    choice = input("Do you want to play again? (Y/N): ").strip().upper()
    if choice == "Y":
        return True
    elif choice == "N":
        return False
    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")


def main_game():
    intro_display()
    word_length = ask_word_length()
    api_url = f'https://random-word-api.vercel.app/api?words=1&length={word_length}&type=uppercase'
    secret = fetch_api_data(api_url)
    # secret = "CIVIL"
    print(secret)
    guess = 0
    while True:
        user = user_word()
        guess += 1
        if guess % 3 == 0:
            clear_terminal()
        secret_letters = split_string(secret)
        user_letters = split_string(user)

        if check_length(user_letters, word_length):
            if check_real_word(user):
                compare_letters(
                    user_letters, secret_letters, wrong_letters)

                if secret_letters == user_letters:
                    print(
                        BM+f"Well Play, you guessed the word {secret} in only {guess} times")
                    return
        print(Back.BLUE+f"Number of guesses: {guess}")
        give_up = input("Do you want to give up? (y/n): ")
        if give_up.lower() == 'y':
            print(f"The secret word was {secret}. Better luck next time!")
            return


def clear_terminal():
    if os.name == 'posix':  # for Unix-like systems (Linux, macOS)
        os.system('clear')
    else:  # for Windows
        os.system('cls')


def main():
    while True:
        clear_terminal()
        main_game()
        if not play_again():
            break
    print("Thanks for playing!")


main()
