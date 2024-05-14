"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from deep_translator import GoogleTranslator
f_strru = []
with open(r'D:\!Обучение\Python start\python_basics\Урок 5. Практическое задание\task_1\my_file.txt') as str_f:
    f_strs = str_f.readlines()
    f_strs1 = [el[:-1] for el in f_strs[:-1]]
    for el in f_strs1:
        translated = GoogleTranslator(source='auto', target='ru').translate(el)
        f_strru.append(translated)
strru_f = open('my_fileru.txt', 'w', encoding='utf-8')
for ind, el in enumerate(f_strru, 1):
    print(el, file=strru_f)
strru_f.close()
