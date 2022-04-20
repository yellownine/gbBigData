"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def __init__(self):
        self.title = type(self).__name__

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(self.title + ": " + "Запуск ручки")


class Pencil(Stationery):

    def draw(self):
        print(self.title + ": " + "Запуск карандаша")


class Handle(Stationery):

    def draw(self):
        print(self.title + ": " + "Запуск маркера")


statClasses = [Pen, Pencil, Handle]

for statCl in statClasses:
    statCl().draw()
