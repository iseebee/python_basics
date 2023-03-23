"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


import random

with open("text5.txt", "w+") as f_str:
    for i in range(random.randint(1, 10)):
        f_str.write(str(random.randint(1, 100)) + ' ')
f_sum = 0
with open("text5.txt") as f_str:
    for i in f_str.read().split():
        f_sum += int(i)
print(f_sum)
