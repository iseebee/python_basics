"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Comp_num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Comp_num(a, b)
    
    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return Comp_num(a, b)
    
    def __str__(self):
        return f'{self.a} + {self.b}i'
    
    
c = Comp_num(3, 2)
d = Comp_num(6, 8)
print(f'Первое число: с = {c}')
print(f'Второе число: d = {d}')
print(f'Сумма чисел: с + d = {c + d}')
print(f'Умножение чисел: с * d = {c * d}')
