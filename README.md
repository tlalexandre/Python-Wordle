# Wordle Game

A classic Wordle game written in Python and played on a terminal based window.

![ScreenshotApp](https://github.com/tlalexandre/Python-Wordle/assets/120526785/7f1d7912-ebbb-4249-93c6-73ef4051694b)


- This simple game has standard rules for Wordle game, there is a secret word that needs to be guessed by inputting words of the same length. If the letters of the word exists in the secret word and are at the right place , they will be displayed with a green background. If they exist in the secret word but misplaced, they'll be displayed  with a yellow background. If they don't exist in the word, they'll be displayed with a red background.
  
- Link to the website: https://python-wordle-3bbb5fe346f5.herokuapp.com/
1. User Experience
2. Existing Features
   1. Introduction Section
   2. Gameplay Section
   3. Give Up Section
   4. Winning Section
   5. Replay Section
3. Testing
4. Bugs Encountered
5. Technologies and Languages. Frameworks & Libraries
6. Deployment
7. Credits
8. Content
9. Media

## User Experience

The primary goal of Python Wordle is to provide a concise application that allows users to play the game of Wordle. 

This site is designed with user experience in mind:

- User wants to enjoy playing a word game.
- User wants to win the game and get a winning notification when it's achieved
- User wants to have clear feedback when they input different words.
- Provides clear error messages to help the user input the correct values expected.

## Existing Features

- Introduction section

  - Once the game starts, it will display the Wordle graphic , and explain him the rules of the game. 

  - The user is asked to choose the length of the word between 4 and 8.

  - Then the user is asked to input his first try.

  ![Introduction](https://github.com/tlalexandre/Python-Wordle/assets/120526785/5da26624-3c90-4dec-a7e9-b6505c6720ec)


- Gameplay section

![WordInputAndDesiredLength](https://github.com/tlalexandre/Python-Wordle/assets/120526785/59927aa7-af12-41ce-b6d0-85f00b48ee26)

  - This is the main section of the game . 
    A random word is selected from an API depending on the length that the users inputs. 
  - Then the user has to input his word. This word will be check through a dictionary API that will check if the user word does exists.
  - If the word does exists, it will be analysed by the code and each of the letters of the user word will be compared to the secret word ones. Depending on if they match, are misplaced or are wrong , a feedback to the user will be done via differents colors .

![Guess](https://github.com/tlalexandre/Python-Wordle/assets/120526785/196d93df-6535-4cf7-9f6e-f9cf5c6e3b58)


- Give Up section

  - After 5 tries, if the user wants to draw a new word or just get the answer, a Give up option is offered. The user has to answer by Yes or No. Only the answer Yes allows the user to get out of the game loop, any other answer will just keep the game running.

    ![GiveUp](https://github.com/tlalexandre/Python-Wordle/assets/120526785/d930d359-6033-4ca9-a7f6-99ddfe3ff9a5)


- The Winning Condition
  - Once the user guessed the secret word, it will be told in how much guesses he found the word and what was the secret word.
 
    ![Win](https://github.com/tlalexandre/Python-Wordle/assets/120526785/811e8dfb-55f8-4a37-8faa-2d18352e4351)

- The Replay Section
  - Once the user won, he's offered to replay the game , by inputting either Y or N , to allow him to replay a game of Wordle.

## Testing

- Validator
  - Using the validator from Code Institute, the code runs with no error. 
    The trailing space mentionned in the results are due to the ASCII Logo in the introduction of the game. 

![Pep8Validator](https://github.com/tlalexandre/Python-Wordle/assets/120526785/abb704c2-e3c9-4a97-9a45-73ecf9b384a5)


- Error Handling
  - Through the code, I implemented several error handling cases . Here is a list of them:
  
    - When the user has to input the length of the word he desires to play on, if the input is not a number, the following error message is displayed, and the user is asked to input again:
  
    ![ErrorWordLength](https://github.com/tlalexandre/Python-Wordle/assets/120526785/1623cb2b-dbda-41dc-be67-7e4806b41b2e)

    - When the user has to input a word, the word is compared to an API that's a dictionary, to make sure the word exist. If it doesn't, the user get the following message and is asked to input a new word:
  
    ![ErrorWordDoesNotExist](https://github.com/tlalexandre/Python-Wordle/assets/120526785/8eba9be5-d579-46e7-b15e-6a7000a63dfd)

    - When the user has to input a word, the program will check if the length of the user word matches the length picked at the start of the game to unsure that the comparison between the secret word and the user word       is done properly. If the user word is too long, the program will return the following message:
    
    ![ErrorWordTooLong](https://github.com/tlalexandre/Python-Wordle/assets/120526785/34c6e3b0-8a6e-48a9-9fc7-e7d98beb002f)

    - When the user is asked if he wants to play a new game, he has to confirm by inputting either "Y" or "N".If anything else is input , the user gets the following message:
   
      ![ErrorPlayAgain](https://github.com/tlalexandre/Python-Wordle/assets/120526785/4c3f3625-73ec-4291-ac14-a0a1d95c530b)

### Bugs encountered

- I encountered only one major bug, when the user would input a word containing a double letter such as "APPLE" and the secret word only contains single letters (ex:"AMPLE"), the program would return the first "P" of "APPLE" as a misplaced letter. 

  - Fixing: 
    To fix that issue, I added on top of the comparison of the letters of each word between themselves, a system that would count the iterations of each letter in both words. 
    So in this example, "APPLE" would return something like this:
    "A"=1 "P"=2 "L"=1 "E"=1

    And "AMPLE" would return 1 for each letter.

    Then, I just need to compare the number of iterations of each letter between the two words, and any extra iteration of a letter is put as a wrong letter.

### Technologies, Languages & Libraries

- Python3 is the only language used in this project.
- The different libraries used in this program are :
  - OS to allow to clear the terminal every 3 guesses
  - Colorama to display letters in color.
  - Requests to be able to fetch APIs
- The Code Institute's full template for Python is used for the program to display properly the terminal in the deployed site on Heroku.
- Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- Github is used to store the project code after being pushed from Git
- Heroku is used to build, run and scale applications in a similar manner across most languages.

### Deployement

- Go to Heroku Dashboard
- Click New
- Select to create a new app
- Set the buildbacks to Python then to NodeJS
- Link the Heroku app to the Github repository
- Click on Deploy

### Credits

- Student support guided me on how to fix the bug I encountered.

### Medias

- Unsplash, for the background picture of the website.

- Chat GPT, to help me put down my logic into code.

- ASCII art:http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

  To create the logo of the game.

​	



