"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""
import sys
sys.path.append('../task1')
import helpers


userChoice = input('Как будем решать задачку? Через список (1) или через словарь (2)? ')

if (userChoice == "1"):
    seasons = ['зима', 'весна', 'лето', 'осень']
elif (userChoice == "2"):
    seasons = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень'}
else:
    print('Надо было выбрать 1 или 2 :(')
    sys.exit(1)

month = helpers.getUserNumber('Введите номер месяца: ')
if (month > 12 or month <= 0):
    print('Так не бывает!')
    sys.exit(1)
else:
    seasonNumber = (month - 1) // 3
    season = seasons[seasonNumber]
    print(season)
