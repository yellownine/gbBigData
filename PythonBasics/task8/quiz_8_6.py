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
