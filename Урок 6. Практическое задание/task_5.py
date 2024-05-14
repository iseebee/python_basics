"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ''

    def draw(self):
        print(f'Запуcк отрисовки: ')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print(f'{self.title} - Pen.')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(f'{self.title} - Pencil.')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print(f'{self.title} - Handler. ')


stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
