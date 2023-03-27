"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from itertools import cycle
import time


class Trafficlight:
    __color = ''

    def running(self, turns):
        tr_colors = ['Red', 'Yellow', 'Green']
        i = 1
        for el in cycle(tr_colors):
            __color = el
            print(__color)
            i += 1
            if __color == 'Red':
                time.sleep(7)
            elif __color == 'Yellow':
                time.sleep(2)
            elif __color == 'Green':
                time.sleep(1)
            if i > turns:
                break


tr_light = Trafficlight()
tr_light.running(int(input('Введите кол-во переключений светофора: ')))
