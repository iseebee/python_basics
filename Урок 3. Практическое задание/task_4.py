"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x, y):
    res = 1
    for i in range(1, -1*(y-1)):
        res = res * x
        i += 1
    print(y, 1 / res)


my_func(float(input('Число X')), int(input('Число Y')))
