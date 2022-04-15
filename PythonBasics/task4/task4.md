# Практическое задание. Урок 4
---
[Задание 1](quiz_4.1.py)  
```python
"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

[hours, rate, premium] = sys.argv[1:4]
try:
    [hours, rate, premium] = [int(hours), float(rate), float(premium)]
except ValueError:
    print('Аргументы скрипта имеют неверный формат')
    sys.exit(1)


def salary(hours, rate, premium):
    return hours * rate + premium


print('Заработная плата сотрудника %0.2f' % salary(hours, rate, premium))
```
---
[Задание 2](quiz_4.2.py)  
```python
"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

sourceData = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# 1
def filterArray(array):
    result = []
    for i in range(1, len(array)):
        first = array[i-1]
        second = array[i]
        if second > first:
            result.append(second)
    return result


# 2
result = [sourceData[i] for i in range(1, len(sourceData)) if sourceData[i] > sourceData[i-1]]


print(filterArray(sourceData))
print(result)
```
---
[Задание 3](quiz_4.3.py)  
```python
"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""

result = [n for n in range(20, 240) if (n % 20 == 0 or n % 21 == 0)]
print(result)
```
---
[Задание 4](quiz_4.4.py)  
```python
"""
Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию.
Элементы выведите в порядке их следования в исходном списке.
Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

sourceData = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [i for i in sourceData if sourceData.count(i) == 1]
print(result)
```
---
[Задание 5](quiz_4.5.py)  
```python
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
```
---
[Задание 6](quiz_4.6.py)  
Мне видится так лучше, чем оборачивать count/cycle в какой-то цикл с проверкой потому, что обертка не будет итератором
```python
"""
Реализовать два небольших скрипта:
 - итератор, генерирующий целые числа, начиная с указанного;
 - итератор, повторяющий элементы некоторого списка, определённого заранее.

Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения.
#### Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""


class SimpleIterator:
    def __init__(self, start, limit):
        self.limit = limit
        self.start = start - 1

    def __iter__(self):
        self.counter = self.start - 1
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


generatorIter = SimpleIterator(3, 10)
for num in generatorIter:
    print(num)


class SimpleRepeater:
    def __init__(self, iterable, limit):
        self.iterable = iterable
        self.limit = limit
        self.period = len(iterable)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.limit:
            next = self.iterable[self.counter % self.period]
            self.counter += 1
            return next
        else:
            raise StopIteration


repeaterIter = SimpleRepeater('ABC', 10)
for el in repeaterIter:
    print(el)
```
---
[Задание 7](quiz_4.7.py)  
```python
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
```
