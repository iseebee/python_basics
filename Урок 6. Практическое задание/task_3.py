"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

    def __str__(self):
        return (f'Работник: {p1.get_full_name()}\nДолжность: {p1.position}\nОклад, руб.: {p1.wage}\n'
                f'Премия, руб.: {p1.bonus}\nК выплате, руб. {p1.get_total_income()}')


p1 = Position('Пупкин', 'Вася', 'Тимлид', 100000, 25000)
print(f'Работник: {p1.get_full_name()}\nДолжность: {p1.position}\nОклад, руб.: {p1.wage}\nПремия, руб.: {p1.bonus}\n'
      f'К выплате, руб. {p1.get_total_income()}\n')

print(p1)
