import random
from colorama import init
init()
from colorama import Fore, Back, Style


with open('example.txt', 'r+', encoding='utf-8') as f:
    words_list = f.read().split()
    length_5 = [i for i in words_list if len(i) == 5]
    word = random.choice(length_5).upper()
    count = 0
    while count < 6:
        text = input().upper()
        if text.lower() in length_5:
            count_yel = 0
            for i in range(len(text)):
                if text[i] not in word:
                    print(Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + text[i], end=' ')
                else:
                    if word.find(text[i]) == i:
                        print(Fore.LIGHTBLACK_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT + text[i], end=' ')
                        count_yel += 1
                    else:
                        print(Fore.LIGHTBLACK_EX + Back.LIGHTWHITE_EX + Style.BRIGHT + text[i], end=' ')
            if count_yel == 5:
                print(Fore.BLACK + Back.CYAN + Style.BRIGHT + 'Вы выиграли, поздравляем!')
                break
        else:
            print(Fore.MAGENTA + Back.RESET +'Такого слова не существует')
            print()
        count += 1
    else:
        print()
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT + f'Вы проиграли. Загаданное слово было {word}')





