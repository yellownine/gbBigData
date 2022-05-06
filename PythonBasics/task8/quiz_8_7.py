"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, ReIm: tuple):
        ComplexNum.__validateType(ReIm)
        self.re = float(ReIm[0])
        self.im = float(ReIm[1])

    @staticmethod
    def __validateType(ReIm: tuple):
        if (not (isinstance(ReIm[0], int) or isinstance(ReIm[0], float)) or
                not (isinstance(ReIm[1], int) or isinstance(ReIm[1], float))):
            raise TypeError('Недопустимый тип для данных: разрешены int и float ')
        else:
            pass

    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return ComplexNum((re, im))

    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return ComplexNum((re, im))

    def __str__(self):
        return f'{self.re} + i*{self.im}'


if __name__ == '__main__':
    c_num_1 = ComplexNum((0,  1))
    c_num_2 = ComplexNum((0.0, 1))
    try:
        c_num_3 = ComplexNum(("df", "300"))
    except Exception as err:
        print(err)

    print(c_num_1 * c_num_2)
    print(c_num_1 + c_num_2)
