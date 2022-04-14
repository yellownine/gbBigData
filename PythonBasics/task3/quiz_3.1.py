"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def derive(numerator, denominator):
    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        print('Вы ввели не числа')
        return
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        if numerator != 0:
            print('На ноль делить нельзя')
            return
        else:
            result = 1
    return result


print(derive(1, 2))
print(derive(0, 2))
print(derive(2, 0))
print(derive("1", "2"))
print(derive(0, 0))
print(derive("a", "B"))
print(derive("b", 0))
