# Практическое задание. Урок 7
---
[Задание 1](quiz_7.1.py)  
```python
"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, arrayData: [[int]]):
        self.arrayData = arrayData
        self.n = len(arrayData)
        self.m = len(arrayData[0])
        for row in arrayData:
            if len(row) != self.m:
                raise ValueError('Неверный формат инициализационных данных')

    def __str__(self):
        res = []
        for row in self.arrayData:
            res.append(" ".join(map(str, row)))
        return "\n".join(res)

    def __add__(self, other):
        res = []
        if (self.n != other.n or self.m != other.m):
            raise ArithmeticError('Матрицы должны иметь одинаковую размерность')
        else:
            for i in range(self.n):
                res.append([sum(x) for x in zip(self.arrayData[i], other.arrayData[i])])
        return Matrix(res)


raw_1 = [list(range(3)) for i in range(3)]
mat_1 = Matrix(raw_1)
print(mat_1 + mat_1)

raw_error = [list(range(3+i)) for i in range(3)]
try:
    Matrix(raw_error)
except Exception as err:
    print(err)

raw_2 = [list(range(4)) for i in range(4)]
try:
    Matrix(raw_1) + Matrix(raw_2)
except Exception as err:
    print(err)

raw_3 = [list(range(-4, 0)) for i in range(4)]
print(Matrix(raw_3) + Matrix(raw_2))
```
---
[Задание 2](quiz_7.2.py)  
```python
"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    __totalCloth: float
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    @abstractmethod
    def countTotalCloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, v: int):
        super().__init__(name, v)
        self.countTotalCloth()

    @property
    def totalCloth(self):
        return self.__totalCloth

    def countTotalCloth(self):
        self.__totalCloth = self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name: str, h: int):
        super().__init__(name, h)
        self.countTotalCloth()

    @property
    def totalCloth(self):
        return self.__totalCloth

    def countTotalCloth(self):
        self.__totalCloth = self.size*2 + 0.3


my_coat = Coat('spring', 180)
my_suit = Suit('work', 48)

print('Необходимое количество ткани: %0.2f' % (my_coat.totalCloth + my_suit.totalCloth))
```
---
[Задание 3](quiz_7.3.py)  
```python
"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class WaterMellonCell:
    __cellCount: int

    def __init__(self, cellCount: int):
        if cellCount <= 0:
            raise ValueError('Число ячеек клетки должно быть больше 0')
        elif not isinstance(cellCount, int):
            raise TypeError('Неверный тип для задания числа ячеек')
        self.__cellCount = cellCount

    @property
    def cellCount(self):
        return self.__cellCount

    def __add__(self, other):
        totalcells = self.cellCount + other.cellCount
        # / Хорошо бы удалить инстрансы self и other, но это, похоже невозможно:()
        return WaterMellonCell(totalcells)

    def __sub__(self, other):
        totalcells = self.cellCount - other.cellCount
        if totalcells <= 0:
            print('Операция вычитания такой последовательности Клеток недопустима')
        else:
            return WaterMellonCell(totalcells)

    def __mul__(self, other):
        totalcells = self.cellCount*other.cellCount
        return WaterMellonCell(totalcells)

    def __truediv__(self, other):
        totalcells = self.cellCount//other.cellCount
        if totalcells > 0:
            return WaterMellonCell(totalcells)
        else:
            print('Чпок')

    def make_order(self, numInRow: int):
        totalcells = self.cellCount
        while totalcells > 0 and totalcells > numInRow:
            print("*"*numInRow)
            totalcells -= numInRow
        print("*"*totalcells)


cell_1 = WaterMellonCell(13)
cell_2 = WaterMellonCell(10)
try:
    print((cell_1+cell_2).cellCount)
    print((cell_1-cell_2).cellCount)
    print((cell_1*cell_2).cellCount)
    print((cell_2/cell_1).cellCount)
except Exception as err:
    print(err)

cell_1.make_order(4)
```
