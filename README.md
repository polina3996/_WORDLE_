# _WORDLE_
A game on Python
A user tries to guess a word of 5 letters,which was concieved by module 'random', by entering his variants. The module uses a file of nouns. If there are words not of 5 letters in the file, the program must sort the file.
The user has 6 efforts.
The game also checks whether the entered word exists by searching for it in the file and does not accept nonexistent words.
If the letter in an entered word is non correct, is correct or also the position of the letter is correct, the program highlights this letter with the corresponding color with the help of module 'colorama'.
When all the letters in the entered word and their positions are correct, the user wins.
After 6 efforts, if there were no winning, the user loses.
