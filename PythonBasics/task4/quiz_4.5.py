"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

generatedData = (i for i in range(100, 1001) if (i % 2 == 0))


def reducer(a, b):
    return a * b


result = reduce(reducer, generatedData, 1)
print(result)
