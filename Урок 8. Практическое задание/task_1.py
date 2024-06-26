"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def number(cls, day_month_year):
        lst = list(day_month_year.split('.'))
        Data.day = int(lst[0])
        Data.month = int(lst[1])
        Data.year = int(lst[2])

    @staticmethod
    def valid():
        if Data.day < 0 or Data.day >= 32:
            return f'Нет такого дня'
        if Data.month < 0 or Data.month >= 13:
            return f'Нет такого месяца'
        else:
            return f'Текущая дата {Data.day}.{Data.month}.{Data.year}'


Data.number("31.12.2023")
print(Data.valid())
