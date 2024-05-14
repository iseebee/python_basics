"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, m_dim, *args):
        self.m_dim = m_dim
        n_row = 0
        self.row = []
        self.col = []
        self.m_args = []
        for i in args:
            self.m_args.append(i)
        while n_row < self.m_dim:
            el = 0
            while el < self.m_dim:
                self.row.append(self.m_args[el])
                el += 1
            self.col.append(self.row)
            self.row = []
            n_row += 1
            j = 0
            while True:
                i = 0
                self.m_args.pop(i)
                j += 1
                if j == self.m_dim:
                    break

    def __str__(self):
        i = 0
        m_str = ''
        while i < self.m_dim:
            m_str = m_str + '\t'.join(map(str, self.col[i])) + '\n'
            i += 1
        return m_str

    def __add__(self, other):
        summ = self.col
        res = []
        res1 = [other.m_dim]
        for a in range(len(self.col)):
            for b in range(len(self.col[a])):
                summ[a][b] = self.col[a][b] + other.col[a][b]
        for a in range(len(self.col)):
            for b in range(len(self.col[a])):
                res.append(summ[a][b])
        args2 = res
        return Matrix(other.m_dim, *args2)


dim1 = int(input('Введите кол-во столбцов(рядов) складываемых квадратных матриц'))
args = map(int, (input(f'Введите значения 1-ой матрицы слева направо сверху вниз через пробел: ').split(' ')))
m1 = Matrix(dim1, *args)
args1 = map(int, (input(f'Введите значения 2-ой матрицы слева направо сверху вниз через пробел: ').split(' ')))
m2 = Matrix(dim1, *args1)

print(m1 + m2)
