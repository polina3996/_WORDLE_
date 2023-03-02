import random
from colorama import init
init()
from colorama import Fore, Back, Style

#файл со словами, откуда вы будете случайным образом выбирать слово для игры.
with open('example,txt', 'r+', encoding='utf-8') as f:
    words_list = f.read().split()
    length_5 = [i for i in words_list if len(i) == 5] #нужно сперва исключить слова, длина которых не равна 5
    word = random.choice(length_5).upper()  #рандомно выбираем загаданное слово из списка в верхнем регистре
    count = 0 #счетчик попыток
    while count < 6:  #имеем 6 попыток
        text = input().upper() #вводим слово
        if text.lower() in length_5: #проверяем, существует ли слово(=есть ли в файле)
            count_yel = 0
            for i in range(len(text)):
                if text[i] not in word:  #буквы нет в загаданном слове
                    print(Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + text[i], end=' ')  #на сером фоне белая буква
                else:  #буква есть в загаданном слове
                    if word.find(text[i]) == i: #совпало по индексу
                        print(Fore.LIGHTBLACK_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT + text[i], end=' ')  # на желтом фоне черная буква
                        count_yel += 1
                    else:  #не совпало по индексу
                        print(Fore.LIGHTBLACK_EX + Back.LIGHTWHITE_EX + Style.BRIGHT + text[i], end=' ')  # на белом фоне черная буква
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





