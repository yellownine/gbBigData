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
