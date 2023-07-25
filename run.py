# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from IPython.display import clear_output
from colorama import Fore, Back, init
import requests
init(autoreset=True)

G = Back.LIGHTGREEN_EX
R = Back.RED
B = Back.CYAN
Y = Back.YELLOW
W = Back.WHITE
M = Back.MAGENTA
ENDC = Back.RESET


def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                word_string = data[0]
                print(word_string)
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


api_url = 'https://random-word-api.vercel.app/api?words=1&length=5&type=uppercase'


def intro_display():
    print(B+"Welcome to Python Wordle\n")
    print(B+"Press Enter to start")
    print(B+"The rules are simple: Guess the Wordle in 6 tries.\n Each guess must be a 5-letter word.\n Try to input differents letters and see if they exist in the word.\n If the letter does exist in the word and in the correct spot,\n it will display in "+(G+"GREEN\n"))
    print("If the letter exists in word but is misplaced it will turn "+(Y+"YELLOW\n"))
    print(G+"If the letter doesn't exist in the word, it will turn " +
          (R+"RED\n"))

    print(W+"Good Luck !")


def user_word():
    user_input = input("Enter your word: ").upper()
    return user_input


def split_string(word):
    letters = []
    for letter in word:
        letters.append(letter)
    return letters


def check_length(user_letters):
    if len(user_letters) != 5:
        print("You can only enter up to 5 letters.")
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
    print(M +
          f"Well Play ! You guessed in only {guess} times to find the word: {secret}")


wrong_letters = set()


def compare_letters(secret_letters, user_letters, wrong_letters, guess):
    '''
    Creates a set with the letters from the user and the one from the secret word. 
    Iterates through the user_letters, if the letter exists , it triggers the second condition checking the position of the letters. 
    If they're identical, return an answer about right letter and right position
    If they have different positions but same letters, return an answer right letter wrong position. 
    If completely different, return answer, does not exist in the word
    '''

    secret_letters = list(secret_letters)
    user_letters = list(user_letters)
    common_letters = set(secret_letters) & set(user_letters)

    if secret_letters == user_letters:
        victory(guess, secret)
    else:
        correct_positions = set()
        misplaced_positions = set()
        for letter in user_letters:
            if letter in common_letters:
                position_secret = [i for i, x in enumerate(
                    secret_letters) if x == letter]
                position_user = [i for i, x in enumerate(
                    user_letters) if x == letter]
                for pos_secret in position_secret:
                    for pos_user in position_user:
                        if pos_secret == pos_user:
                            correct_positions.add(pos_user)
                        else:
                            misplaced_positions.add(pos_user)
        for i, letter in enumerate(user_letters):
            if letter in common_letters:
                if i in correct_positions:
                    print(G+f"{letter}"+ENDC, end="")
                elif i in misplaced_positions:
                    print(Y+f"{letter}"+ENDC, end="")
            else:
                print(R + f"{letter}"+ENDC, end="")
                wrong_letters.add(letter)
        print("\n")
    print(
        R+f"Here is a list of the letters you already tried and are wrong: \n {wrong_letters}")
    print("\n")
    return wrong_letters

    #             if position_secret == position_user:

    #                 print(G+f"{letter}"+ENDC, end="")


    #             else:
    #                 print(Y+f"{letter}"+ENDC, end="")
    #         else:
    #             print(R+f"{letter}"+ENDC, end="")
    #             wrong_letters.add(letter)
    #     print("\n")
    # print(
    #     R+f"Here is a list of the letters you already tried and are wrong: \n {wrong_letters}")
    # print("\n")
    # return wrong_letters
secret = fetch_api_data(api_url)
guess = 0

intro = intro_display()


def main(guess):
    user = user_word()
    secret_letters = split_string(secret)
    user_letters = split_string(user)
    if check_length(user_letters):
        if check_real_word(user):
            compare_letters(secret_letters, user_letters, wrong_letters, guess)
    guess += 1
    print(Back.BLUE+f"You guessed {guess} times")
    main(guess)
    return guess


main(guess)
