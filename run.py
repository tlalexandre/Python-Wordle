# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore
import requests

word_string = ""


def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                word_string = data[0]
                print(f"Extracted word: {word_string}")
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


api_url = 'https://random-word-api.herokuapp.com/word?length=5'
secret = fetch_api_data(api_url)

if secret:
    print(secret)

print(Fore.CYAN+"Welcome to Python Wordle\n")
print(Fore.BLUE+"Press Enter to start")
print(Fore.GREEN+"The rules are simple: Guess the word on the screen in the less tries possible.\n Try to input differents letters and see if they exist in the word.\n If the letter exists in word but is misplaced it will turn"+(Fore.YELLOW+" YELLOW\n"))

print(Fore.GREEN+"If the letter doesn't exist in the word, it will turn" +
      (Fore.RED+" RED\n"))

print(Fore.GREEN+"Good Luck !")


user = "point"


def split_string(word):
    letters = []
    for letter in word:
        letters.append(letter)

    print(f"{letters} for the word {word}\n")
    return letters


secret_letters = split_string(secret)
user_letters = split_string(user)


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
                    print(f"{letter} right and at the right position")
                else:
                    print(f"{letter} right but not at the right position")
            else:
                print(f"{letter} does not exist in the word")


compare_letters(secret_letters, user_letters)
