"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
import sys


def sumUserNumbersSequently(stopSymbol, result=0):
    numberSeq = input('Введите через пробел несколько числе и нажмите Enter.\n' + f'Если хотите закончить, введите {stopSymbol}\n')
    if numberSeq == stopSymbol:
        return result
    userNumbers = numberSeq.split(" ")
    for num in userNumbers:
        if num == stopSymbol:
            print(result)
            sys.exit(0)
        try:
            result += int(num)
        except ValueError:
            print(f'Это же {num} не чило!')
            sys.exit(1)
    print(result)
    sumUserNumbersSequently(stopSymbol, result)


userStopSymbol = input("Введите символ (без пробела), который введете, когда заходите закончить: ")
sumUserNumbersSequently(userStopSymbol)
