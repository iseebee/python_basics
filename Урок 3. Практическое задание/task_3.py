"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func1(x, y, z):
    mas = [x, y, z]
    mas.sort(reverse=True)
    res = mas[0] + mas[1]
    return res


def my_func2(x, y, z):
    res = x + y + z - min(x, y, z)
    return res


a = int(input('введите число: '))
b = int(input('введите число: '))
c = int(input('введите число: '))
print(my_func1(a, b, c))
print(my_func2(a, b, c))
