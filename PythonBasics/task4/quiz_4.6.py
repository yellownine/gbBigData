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
