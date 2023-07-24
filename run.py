# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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
    print(G+"The rules are simple: Guess the word on the screen in the less tries possible.\n Try to input differents letters and see if they exist in the word.\n If the letter exists in word but is misplaced it will turn "+(Y+"YELLOW\n"))
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


def add_guesses(secret_letters, user_letters):
    compare_letters(secret_letters, user_letters)


def victory(guess, secret):
    print(M +
          f"Well Play ! You guessed in only {guess} times to find the word: {secret}")


def compare_letters(secret_letters, user_letters):
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
        for letter in user_letters:
            if letter in common_letters:
                position_secret = secret_letters.index(letter)
                position_user = user_letters.index(letter)
                if position_secret == position_user:

                    print(G+f"{letter}"+ENDC, end="")
                    secret_letters[position_secret] = None
                    user_letters[position_user] = None

                else:

                    print(Y+f"{letter}"+ENDC, end="")
                    secret_letters[position_secret] = None
            else:
                print(R+f"{letter}"+ENDC, end="")
    print("\n")


secret = fetch_api_data(api_url)
guess = 0

intro = intro_display()


def main(guess):
    user = user_word()
    secret_letters = split_string(secret)
    user_letters = split_string(user)
    compare_letters(secret_letters, user_letters)
    guess += 1
    print(Back.BLUE+f"You guessed {guess} times")
    main(guess)


main(guess)
