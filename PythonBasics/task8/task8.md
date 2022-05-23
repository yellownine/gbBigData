# Практическое задание. Урок 8
---
[Задание 1](quiz_8_1.py)  
```python
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

```
---
[Задание 2](quiz_8_2.py)  
```python
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivision(Exception):
    def __str__(self):
        return 'Деление на ноль недопустимо'


try:
    num, den = input('Введите числитель и знаменатель через пробел: ').split(" ")
    if den == "0":
        raise ZeroDivision()
except ZeroDivision as err:
    print(err)

print('Несмотря на ошибку, программа ее обработала и продолжает корректно функционировать.')

```
---
[Задание 3](quiz_8_3.py)  
```python
"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
import sys


class InputController:
    nums: [int] = []

    def __init__(self, stopWord: str):
        if (stopWord == ""):
            raise ValueError('Некорректный набор символов для остановки алгоритма!')
        else:
            self.stopWord = str(stopWord)

    def run(self):
        print(sys.platform + ': Запущен контроллер ввода')
        self.__query()

    def __query(self):
        inputChars = ""
        while inputChars != self.stopWord:
            inputChars = input('Введите число: ')
            try:
                num = float(inputChars)
                self.nums.append(num)
            except ValueError:
                print('Вы ввели не число!')
        if (len(self.nums) != 0):
            print(self.nums)
            sys.exit(0)
        else:
            print('Вы не ввели ни одного числа')
            sys.exit(1)


if __name__ == '__main__':
    inputControllerService = InputController("stop")
    inputControllerService.run()

```
---
[Задание 4](quiz_8_4.py)  
```python
"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


class Store:

    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address
        self._storeProducts = {}

    @property
    def name(self):
        return self.__name

    @property
    def addres(self):
        return self.__addres

    @property
    def storeProducts(self):
        return self._storeProducts

    def dispatchPruduct(self, type: str, quant: int):
        if quant <= 0:
            raise ValueError('Запрошено некорректное количество товара')
        else:
            totalQuant = self.getProductQuant(type)
            if (totalQuant < quant):
                raise ValueError('Товара на складе недостаточно')
            else:
                self._storeProducts[type] -= quant
                return {"type": type, "quantity": quant}

    def getProductQuant(self, type: str):
        try:
            quant = self._storeProducts[type]
            return quant
        except KeyError:
            print("Такого товара еще не было на этом складе")
            return 0

    def loadPruduct(self, type: str, quant: int):
        if (quant < 0):
            raise ValueError('Невозможно загрузить отрицательно количество товара')
        try:
            self._storeProducts[type] += quant
        except KeyError:
            self._storeProducts[type] = quant

    def burnTheStore(self):
        self._storeProducts = {}
        print('Склад сгорел')


class Product:

    def __init__(self, type: str, price: int, model: str):
        self.__type = type
        self.__price = price
        self._model = model
        self._serialNumber = None

    @property
    def type(self):
        return self.__type

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def model(self):
        return self._model

    @property
    def serialNumber(self):
        return self._serialNumber

    @serialNumber.setter
    def serialNumber(self, serial: str):
        if (self._serialNumber):
            raise Exception("Нельзя изменить серийный номер")
        else:
            self._serialNumber = str(serial)

    def __str__(self):
        return f'{self._model}/sn: {self._serialNumber}'


class Printer(Product):

    def __init__(self, price: int, model: str):
        super().__init__('printer', price, model)
        self.__expandMaterials = {}

    @property
    def materials(self):
        return self.__expandMaterials

    @materials.setter
    def materials(self, materials: dict):
        self.__expandMaterials = materials


class Copier(Product):

    def __init__(self, price: int, model: str):
        super().__init__('copier', price, model)
        self.__expandMaterials = {}

    @property
    def materials(self):
        return self.__expandMaterials

    @materials.setter
    def materials(self, materials: dict):
        self.__expandMaterials = materials


class Scanner(Product):
    def __init__(self, price: int, model: str):
        super().__init__('scanner', price, model)


if __name__ == '__main__':

    printer = Printer(100, "hp100")
    copier = Copier(200, "xerox")
    scanner = Scanner(40, "canon")

    print(printer)

    cartridge = {
        "type": "gh100",
        "resource": 2000
    }
    printer.materials = {'cartridge': cartridge}
    copier.materials = {'cartridge': cartridge}
    printer.serialNumber = 10000
    copier.serialNumber = 20001
    scanner.serialNumber = "00020"

    print(scanner.serialNumber)
    print(printer.serialNumber)

    officeEqStore = Store("OfficeEquipment", "Луна, море Дождей")

    officeEqStore.loadPruduct(printer.type, 200)
    officeEqStore.loadPruduct(copier.type, 300)
    officeEqStore.loadPruduct(scanner.type, 100)

    officeEqStore.dispatchPruduct(printer.type, 150)
    print(officeEqStore.storeProducts)
    officeEqStore.dispatchPruduct(copier.type, 150)
    print(officeEqStore.storeProducts)
    officeEqStore.dispatchPruduct(scanner.type, 150)
    print(officeEqStore.storeProducts)

"""
С серийниками, конечно, будет беда. Хорошо бы сделать "Фабрику" техники - допкласс-генератор инстансов
Да и вообще поленился с классом Store. Надо было
- сделать внутренний сервис на основе Фабрики,
- хранить инстансы с серийниками,
- следить в Классе продукта за выпущенным количеством и чтобы серийнки не повторялись (статический атрибуты и методы)
но это все уже долго и мне и проверяющему => пожалел обоих
"""

```
---
[Задание 5](quiz_8_5.py)  
```python
"""
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в
определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""
# Частично это задание уже выполнено в рамказ задачи 4, т.к. я сразу додумал возможный функционал класса Скалада
# Здесь будут некоторые доработки
import random
import datetime
from quiz_8_4 import Store, Printer, Scanner, Copier


class SerialGenerator:
    def __init__(self, serialNumLen: int = 10):
        self.serialNumLen = serialNumLen

    def __iter__(self):
        return self

    def __next__(self):
        serial = [str(random.randint(0, 9)) for i in range(self.serialNumLen)]
        serial = "".join(serial)
        return serial


class ProductFactory:
    def __init__(self):
        self.serialGenerator = SerialGenerator(5)
        self.availableProducts = {
            "printer": Printer,
            "scanner": Scanner,
            "copier": Copier
        }

    def newPruducts(self, type: str, quant: int, model: str):
        productsSet = []
        for i in range(quant):
            product = self.availableProducts[type](0, model)
            product.serialNumber = next(self.serialGenerator)
            productsSet.append(product)
        return productsSet


class OfficeStore(Store):
    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        self._storeProducts: dict = {}
        self._dispatchedPruducts = {}

    def getProductQuant(self, type: str):
        try:
            productSet = self._storeProducts[type]
            return len(productSet)
        except KeyError:
            return 0

    def loadPruducts(self, productsSets: dict):
        for productType in productsSets:
            try:
                self._storeProducts[productType].append(productsSets[productType])
            except KeyError:
                self._storeProducts[productType] = productsSets[productType]
                self._dispatchedPruducts[productType] = []

    def dispatchPruduct(self, type: str, quant: int, destination: str):
        if quant <= 0:
            raise ValueError('Запрошено некорректное количество товара')
        else:
            totalQuant = self.getProductQuant(type)
            if (totalQuant < quant):
                raise ValueError('Товара на складе недостаточно')
            else:
                toDispatch = self._storeProducts[type][:quant]
                self._storeProducts[type] = self._storeProducts[type][quant:]
                self._dispatchedPruducts[type].append({
                    "address": destination, "date": datetime.datetime.now(), "products": toDispatch
                })
                return {"type": type, "productsSet": toDispatch, "address": destination}

    @property
    def dispatchedPruducts(self):
        return self._dispatchedPruducts


if __name__ == '__main__':

    productFactory = ProductFactory()
    printersSet = {"printer": productFactory.newPruducts("printer", 5, "hp")}
    print(printersSet)

    store = OfficeStore('Склад на Луне', "Луна, Море Спокойствия")

    store.loadPruducts(printersSet)

    print(store.dispatchPruduct("printer", 2, "Луна, Море Познания"))

```
---
[Задание 6](quiz_8_6.py)  
```python
"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from quiz_8_5 import ProductFactory as Old_ProductFactory


class ProductFactory(Old_ProductFactory):
    def newPruducts(self, prType: str, quant: int, model: str):
        if (not isinstance(quant, int)):
            raise TypeError(f'Параметр количества должен быть типа int, получен ${type(quant)}')
        else:
            return super().newPruducts(prType, quant, model)


class PrinterFactory(ProductFactory):
    def developePrinters(self, quant: int, model: str):
        return {'printer': super().newPruducts('printer', quant, model)}


class ProductSet:
    def __init__(self, productSet: dict):
        self._productSet = productSet
        self._type = list(productSet.keys())[0]
        self._products = list(productSet.values())[0]

    @property
    def type(self):
        return self._type

    @property
    def products(self):
        return self._products

    def __str__(self):
        strVal = f'{self._type}\n' + "\n".join([pr.__str__() for pr in self._products])
        return strVal


if __name__ == '__main__':
    printerFactory = PrinterFactory()
    productSet = ProductSet(printerFactory.developePrinters(10, 'hp100'))
    print(productSet)

```
---
[Задание 7](quiz_8_7.py)  
```python
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

```
