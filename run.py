# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore, Back, init
import requests
init(autoreset=True)


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
    print(Fore.CYAN+"Welcome to Python Wordle\n")
    print(Fore.BLUE+"Press Enter to start")
    print(Fore.GREEN+"The rules are simple: Guess the word on the screen in the less tries possible.\n Try to input differents letters and see if they exist in the word.\n If the letter exists in word but is misplaced it will turn "+(Back.YELLOW+"YELLOW\n"))

    print(Fore.GREEN+"If the letter doesn't exist in the word, it will turn " +
          (Back.RED+"RED\n"))

    print(Fore.WHITE+"Good Luck !")


def user_word():
    user_input = input("Enter your word: ").upper()
    return user_input


def split_string(word):
    letters = []
    for letter in word:
        letters.append(letter)
    return letters


def compare_letters(secret_letters, user_letters):
    '''
    Creates a set with the letters from the user and the one from the secret word. 
    Iterates through the user_letters, if the letter exists , it triggers the second condition checking the position of the letters. 
    If they're identical, return an answer about right letter and right position
    If they have different positions but same letters, return an answer right letter wrong position. 
    If completely different, return answer, does not exist in the word
    '''

    common_letters = set(secret_letters) & set(user_letters)
    if secret_letters == user_letters:
        print("congratulations you win")
    else:
        for letter in user_letters:
            if letter in common_letters:
                position_secret = secret_letters.index(letter)
                position_user = user_letters.index(letter)
                if position_secret == position_user:
                    print(Back.GREEN +
                          f"{letter}")
                else:

                    print(Back.YELLOW +
                          f"{letter}")
            else:

                print(Back.RED+f"{letter}")


secret = fetch_api_data(api_url)

intro = intro_display()


def main():
    user = user_word()
    secret_letters = split_string(secret)
    user_letters = split_string(user)
    compare_letters(secret_letters, user_letters)
    main()


main()
