"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date: str):
        self.__date = Date.parseDate(date)
        try:
            Date.validateDate(self.__date)
        except ValueError as err:
            print('Объект Date не инициализирован: ' + str(err))

    @property
    def date(self):
        return self.__date

    @classmethod
    def parseDate(cls, date: str):
        dateNum = map(int, date.split("-"))
        day, month, year = dateNum
        return {"day": day, "month": month, "year": year}

    @staticmethod
    def validateDate(date: dict):
        if date["day"] >= 1 and date["day"] <= 30:  # Количество дней в месяце считаем для простоты одинаковым
            pass
        else:
            raise ValueError('Неверно задан день')
        if date["month"] >= 1 and date["month"] <= 12:
            pass
        else:
            raise ValueError('Неверно задан месяц')
        if date["year"] >= 0:
            pass
        else:
            raise ValueError('Неверно задан год')

    def __str__(self):
        return str(self.__date)


date_1 = Date("20-10-2002")
date_2 = Date("40-10-2002")
date_3 = Date("20-0-0")

print(date_1)
