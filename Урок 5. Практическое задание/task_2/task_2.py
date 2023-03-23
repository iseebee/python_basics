"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open('my_file.txt') as str_f:
    f_strs = str_f.readlines()
    f_strs1 = [el[:-1] for el in f_strs[:-1]]
    print(f'Кол-во строк: {len(f_strs1)}')
    for ind, el in enumerate(f_strs1, 1):
        print(ind, len(el))
