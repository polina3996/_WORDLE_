# _WORDLE_
In this game you have 6 tries to guess a 5-letter word, which was selected by module 'random' from a file of nouns. 

The program excludes words not of 5 letters if there are such words in the file.

The game also checks whether the entered word exists by searching for it in the file and does not accept nonexistent words.

Colorama module is used to color input letters to let you know whether they are correct or not

When all the letters in the entered word and their positions are correct, the user wins.

If the word is not guessed in 6 tries, the game is over.

Steps to run the program locally
* Clone the repo
* Run script: pip install -r -requirements.txt
* Start the app: python main.py

Steps to build the game into an executable
* pip install -r -requirements.txt
* pyinstaller 'main.py' --onefile --name 'wordle_game' --clean
* Copy-Item 'example.txt' 'dist/example.txt'

