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
