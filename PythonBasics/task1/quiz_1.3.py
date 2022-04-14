"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
import helpers


def elevenizeNumber(n):
    n = str(n)
    return int(n) + int(n + n) + int(n + n + n)


userNum = helpers.getUserNumber('Введите чилсло: ')

print('Я превратил ваше число в %d' % elevenizeNumber(userNum))
