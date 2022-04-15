"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def factCount(n):
    if n == 1:
        return 1
    else:
        return n * factCount(n-1)


def fact(n):
    for i in range(1, n + 1):
        yield factCount(i)


for el in fact(4):
    print(el)
