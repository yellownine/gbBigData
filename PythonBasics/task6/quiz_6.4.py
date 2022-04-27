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
