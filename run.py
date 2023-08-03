from IPython.display import clear_output
import os
from colorama import Fore, Back, Style, init
import requests

init(autoreset=True)

BG = Style.BRIGHT + Fore.WHITE + Back.GREEN
BR = Style.BRIGHT + Back.RED + Fore.BLACK
FC = Fore.CYAN
BY = Style.BRIGHT + Back.YELLOW + Fore.BLACK
FW = Fore.WHITE
BM = Style.BRIGHT + Back.MAGENTA + Fore.BLACK
ENDC = Back.RESET
FG = Fore.LIGHTGREEN_EXGREEN


def intro_display():
    print(FG + r"""
 __      __                    __   ___              
/\ \  __/\ \                  /\ \ /\_ \             
\ \ \/\ \ \ \    ___    _ __  \_\ \\//\ \       __   
 \ \ \ \ \ \ \  / __`\ /\`'__\/'_` \ \ \ \    /'__`\ 
  \ \ \_/ \_\ \/\ \L\ \\ \ \//\ \L\ \ \_\ \_ /\  __/ 
   \ `\___x___/\ \____/ \ \_\\ \___,_\/\____\\ \____\
    '\/__//__/  \/___/   \/_/ \/__,_ /\/____/ \/____/
                                                     
                                                     

""")

    print(
        FC
        + f"The rules are simple: Guess the Wordle in a minimum of tries.\n")
    print(
        FC
        + f"Try to input real words to find the letters in the secret word.\n"
    )
    print(
        FW
        + "If the letter does exist and at the right place,it will turn in\n"
        + BG
        + " GREEN"
        + Style.RESET_ALL
    )
    print(
        "If the letter exists in the word but is misplaced, it will turn "
        + BY
        + "YELLOW"
        + Style.RESET_ALL
    )
    print(
        FW
        + "If the letter doesn't exist in the word, it will turn "
        + BR
        + "RED"
        + Style.RESET_ALL
    )

    print(FW + "Good Luck !")


def ask_word_length():
    while True:
        try:
            length = int(
                input(FC + "Enter the desired word length(min:4 max:8): "))
            if length < 4 or length > 8:
                print(BR + "Please enter a length between 4 and 8.")
            else:
                return length
        except ValueError:
            print(BR + "Invalid input. Please enter a valid number.")


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
        print(BR + f"You can only enter up to {word_length} letters.")
        return False
    return True


def check_real_word(user):
    try:
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{user}"
        )

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                print(BG + f"The word '{user}' exists in the dictionary.\n")
                return True
            else:
                print(
                    BR
                    + f"The word '{user}' does not exist in the dictionary.")
                return False
        else:
            print(BR + f"The word '{user}' does not exist in the dictionary.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return False


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
        secret_counts[letter] = secret_counts.get(letter, 0) + 1

    for letter in user_letters:
        user_counts[letter] = user_counts.get(letter, 0) + 1

    for i, letter in enumerate(user_letters):
        if letter == secret_letters[i]:
            correct_positions.append(i)

    for i, letter in enumerate(user_letters):
        if letter in secret_letters and i not in correct_positions:
            misplaced_positions.append(i)

    for i, letter in enumerate(user_letters):
        if (letter not in secret_letters) or (user_counts[letter]
                                              > secret_counts[letter]):
            wrong_positions.append(i)
            wrong_letters.add(letter)

    for i, letter in enumerate(user_letters):
        if i in correct_positions:
            print(BG + f"{letter}")
        elif i in misplaced_positions and i not in wrong_positions:
            print(BY + f"{letter}")
        elif i in wrong_positions:
            print(BR + f"{letter}")
    print("\n")
    print(BM + f"Here's the letters you tried and were wrong: {wrong_letters}")
    print("\n")
    return wrong_letters


def play_again():
    choice = input("Do you want to play again? (Y/N): ").strip().upper()
    if choice == "Y":
        return True
    elif choice == "N":
        return False
    else:
        print(BR + "Invalid choice. Please enter 'Y' or 'N'.")


def main_game():
    intro_display()
    word_length = ask_word_length()
    api_url = (
        f"https://random-word-api.vercel.app/api?words=1"
        f"&length={word_length}&type=uppercase"
    )
    secret = fetch_api_data(api_url)
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
                compare_letters(user_letters, secret_letters, wrong_letters)

                if secret_letters == user_letters:
                    print(
                        BM
                        + f"Well Play !Guesses: {guess}. Secret word: {secret}"
                    )
                    return
        print(Back.BLUE + f"Number of guesses: {guess}")
        if guess > 5:
            give_up = input("Do you want to give up? (y/n): ")
            if give_up.lower() == "y":
                print(f"The secret word was {secret}. Better luck next time!")
                return


def clear_terminal():
    if os.name == "posix":  # for Unix-like systems (Linux, macOS)
        os.system("clear")
    else:  # for Windows
        os.system("cls")


def main():
    while True:
        clear_terminal()
        main_game()
        if not play_again():
            break
    print("Thanks for playing!")


main()
