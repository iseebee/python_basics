"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroEx(Exception):
    def __init__(self, txt):
        self.txt = txt


x = int(input('Введите число: '))
y = int(input('Ведите второе число: '))
try:
    if y == 0:
        raise ZeroEx('Деление на ноль!')
    else:
        print(f"Результат: {x / y}")
except ZeroEx as ex:
    print(ex)

