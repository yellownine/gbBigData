"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""


def my_func(var_1, var_2, var_3):
    array = [var_1, var_2, var_3]
    array.sort()
    return array[2] + array[1]


print(my_func(-3, 10, 30))
