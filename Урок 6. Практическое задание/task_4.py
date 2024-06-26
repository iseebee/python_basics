"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Создан автомобиль {name}, цвет {color}')

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self, speed):

        self.speed = speed
        print(f'Скорость движения {self.speed} км/ч')



class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это обычная машина')

    def show_speed(self, speed):

        self.speed = speed
        super().show_speed(self.speed)
        if self.speed > self.max_speed and not self.is_police:
            print('Превышение скорости!')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это спортивная машина')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это служебная машина')

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)
        if self.speed > self.max_speed and not self.is_police:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        print(f'Это полицейская машина')


my_family_car = TownCar(60, 'черный', 'Nissan', False)
my_family_car.go()
my_family_car.show_speed(40)
my_family_car.show_speed(50)
my_family_car.show_speed(70)
my_family_car.turn('направо')
my_family_car.turn('налево')
my_family_car.stop()
print()

my_work_car = WorkCar(40, 'серый', 'Toyota', False)
my_work_car.go()
my_work_car.show_speed(40)
my_work_car.stop()
print()

police_car = PoliceCar(0, 'белый', 'Mitsubisi', True)
print()

sport_car = SportCar(60, 'черный', 'Opel', False)
sport_car.go()
sport_car.show_speed(60)
sport_car.show_speed(70)
police_car.go()
police_car.show_speed(80)
police_car.turn('налево')
police_car.turn('направо')
police_car.stop()
sport_car.stop()
