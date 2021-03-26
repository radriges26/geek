# Реализовать проект «Операции с комплексными числами».

class Complex:
    def __init__(self, com_num):
        self.com_num = com_num

    def __str__(self):
        return f"Коплексное число: {self.com_num}"

    def __add__(self, other):
        return Complex(self.com_num + other.com_num)

    def __mul__(self, other):
        return Complex(self.com_num * other.com_num)


c1 = Complex(1 + 2j)
c2 = Complex(2 + 5j)
c3 = Complex(7 - 1j)

print(c1 + c2 + c3)  # сложение комплексных чисел
print(c1 * c2 * c3)  # умножение комплексных чисел
