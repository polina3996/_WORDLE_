from wordle_ import Wordle
from colorama import Fore, Back, Style, init
init()


with open('example.txt', 'r+', encoding='utf-8') as f:
    print('Welcome to the Wordle. Try guessing a 5 letter word :p')
    print('If you guess a letter and its position, it will be highlighted with Yellow')
    print('If you guess the letter but not its position, it will be highlighted with Grey')
    print('If you don\'t guess the letter, it will remain black')
    print('Now enter your best 5-letter guess!')
    words_list = f.read().split()
    game = Wordle(words_list)
    game.start_game()
    while game.tries_count < 6:
        result = game.handle_input_word(input())
        if result: #tries_count+=1, guess==5
            print(Fore.BLACK + Back.CYAN + Style.BRIGHT + 'You won, congratulations!')
            print(Fore.RESET + Back.RESET + Style.RESET_ALL)
            break
        else: #the word doesn't exist OR #tries_count+=1, guess_count<5
            continue
    else:
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT + f'You lost. The guessed word was {game.word}')
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    


