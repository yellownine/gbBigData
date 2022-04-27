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
