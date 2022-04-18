# Практическое задание. Урок 3
---
[Задание 1](quiz_3.1.py)  
```python
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
```
---
[Задание 2](quiz_3.2.py)  
```python
"""
Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def userInfo(firstname, lastname, year, city, email, phone):
    print(f'имя: {firstname}, фамилия: {lastname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон: {phone}')


userInfo(
    firstname="Иван",
    lastname="Иванов",
    year=2222,
    city="Racoon",
    email="ivan@umbrella.com",
    phone=88899900001
    )
```
---
[Задание 3](quiz_3.3.py)  
```python
"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""


def my_func(var_1, var_2, var_3):
    array = [var_1, var_2, var_3]
    array.sort()
    return array[2] + array[1]


print(my_func(-3, 10, 30))
```
---
[Задание 4](quiz_3.4.py)  
```python
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
```
---
[Задание 5](quiz_3.5.py)  
```python
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
```
---
[Задание 6](quiz_3.6.py)  
```python
"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text
"""


def int_func(userWord):
    return userWord.capitalize()


if __name__ == '__main__':
    print(int_func('userWord'))
```
---
[Задание 7](quiz_3.7.py)  
```python
"""
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""
import imp
import sys

inputArgs = sys.argv

capitalizer = imp.load_source('quiz_3.6', 'quiz_3.6.py').int_func

wordsArray = inputArgs[1: -1]

result = ""
for word in wordsArray:
    result += capitalizer(word) + " "

print(result)
```
