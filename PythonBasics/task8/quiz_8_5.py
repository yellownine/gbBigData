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
