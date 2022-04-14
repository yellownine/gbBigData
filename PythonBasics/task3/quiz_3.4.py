"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
import sys

inputArgs = sys.argv
try:
    base = float(inputArgs[1])
    power = int(inputArgs[2])
    if (base <= 0):
        raise ValueError
    if (power >= 0):
        raise ValueError
except ValueError:
    print('Аргументы, передаваемые программы, должны быть числами: первое - вещественное положительное, второе - целое отрицательное')
    sys.exit(1)


def my_func(_base, _power):
    return _base**_power


def my_func_forStyle(_base, _power):
    result = _base
    while _power < -1:
        result = result * _base
        _power += 1
    return 1/result


print(my_func(base, power))
print(my_func_forStyle(base, power))
