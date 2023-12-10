import random
from colorama import Fore, Back, Style


class Wordle:
    def __init__(self, list_of_words):
        self.words = []
        for word in list_of_words:
            if len(word) == 5:
                self.words.append(word.upper())

    def start_game(self):
        self.tries_count = 0
        self.guessed_count = 0
        self.word = random.choice(self.words)

    def handle_input_word(self, input_word):
        self.guessed_count = 0
        input_word = input_word.upper()
        if input_word not in self.words:
            print(Fore.MAGENTA + Back.RESET +'This is unknown word')
            print()
            return
        for i in range(len(input_word)):
            if input_word[i] not in self.word:
                print(Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + input_word[i], end=' ')
            else:
                if input_word[i] == self.word[i]:
                    print(Fore.LIGHTBLACK_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT + input_word[i], end=' ')
                    self.guessed_count += 1
                else:
                    print(Fore.LIGHTBLACK_EX + Back.LIGHTWHITE_EX + Style.BRIGHT + input_word[i], end=' ')
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)
        self.tries_count += 1
        return self.guessed_count == 5
            


