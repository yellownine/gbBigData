"""
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""
import sys


initialSeq = [7, 5, 3, 3, 2]
userInput = 'null'
while True:
    try:
        userInput = input('Введите любое число. Чтобы закончить введите Enter. ')
        if userInput == "":
            sys.exit(0)
        else:
            userInput = int(userInput)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        sys.exit(1)

    initialSeq.append(userInput)
    initialSeq.sort(reverse=True)
    print('=>',  initialSeq)
