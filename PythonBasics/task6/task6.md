# Практическое задание. Урок 6
---
[Задание 1](quiz_6.1.py)  
```python
"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time
from itertools import cycle


class TrafficLight:
    __color = cycle(["красный", "желтый", "зеленый"])

    def running(self):
        while True:
            self.__swithcMode(7)
            self.__swithcMode(2)
            self.__swithcMode(5)

    def __swithcMode(self, duration):
        color = next(self.__color)
        print(color)
        time.sleep(duration)


trafficLight = TrafficLight()
trafficLight.running()
```
---
[Задание 2](quiz_6.2.py)  
```python
"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massCount(self, asfaltDensity, coverHight):
        totalAsfaltWeight = self._length * self._width * asfaltDensity * coverHight
        return(totalAsfaltWeight)


road = Road(5000, 20)
print(road.massCount(25, 5))
```
---
[Задание 3](quiz_6.3.py)  
```python
"""
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return " ".join([self.name, self.surname])

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


me = Position(
    name="Leonid",
    surname="Aronov",
    position="Junior FullStack",
    income={"wage": 100, "bonus": 50}
)

print(me.get_full_name() + f' has salary {me.get_total_income()}')
print(me.__dict__)

```
---
[Задание 4](quiz_6.4.py)  
```python
"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed: int, color: str, name="Car", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.color} {self.name} составляет {self.speed}')


class TownCar(Car):
    speed_limit = 60

    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, name="TownCar")

    def show_speed(self):
        if(self.speed > self.speed_limit):
            print(f'{self.color} {self.name} превышает скорость')
        else:
            Car.show_speed(self)


class WorkCar(Car):
    speed_limit = 40

    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, name="WorkCar")

    def show_speed(self):
        if(self.speed > self.speed_limit):
            print(f'{self.color} {self.name} превышает скорость')
        else:
            Car.show_speed(self)


class SportCar(Car):
    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, name="SportCar")


class PoliceCar(Car):
    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, name="PoliceCar", is_police=True)


def testCarClass(car: Car):
    print(car.__dict__)
    car.show_speed()
    car.go()
    car.stop()
    car.turn('left')
    car.turn('right')


color = ["red", "green", "white"]
speed = [10, 50, 100]

for c in color:
    for s in speed:
        testCarClass(SportCar(s, c))
        testCarClass(WorkCar(s, c))
        testCarClass(TownCar(s, c))
        testCarClass(PoliceCar(s, c))
```
---
[Задание 5](quiz_6.5.py)  
```python
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
```
