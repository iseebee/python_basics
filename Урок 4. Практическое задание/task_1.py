"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv

working_hour, rate_s, bonus = map(int, argv[1:])
print(f' Заработная плата сотрудника за расчетный период: {working_hour * rate_s + bonus}')
