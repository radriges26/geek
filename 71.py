"""
Реализовать класс Matrix (матрица).
Реализовать перегрузку методов:
__init__ (инициализация)
__str__ (вывод)
 __add__ (сложение)
"""


class Matrix:
    def __init__(self, mx):
        self.mx = mx

    def __str__(self):
        return f"Матрица это список списков: {self.mx}"

    def __add__(self, other):
        for i in range(len(self.mx)):
            for j in range(len(self.mx[i])):
                self.mx[i][j] = self.mx[i][j] + other.mx[i][j]
        return Matrix(self.mx)


a = [[1, 2, 3], [4, 5, 6], [0, 0, 1]]
b = [[0, -1, 5], [7, 2, 9], [0, 1, 0]]
c = [[2, 2, 2], [2, 2, 2], [1, 0, 0]]

m1 = Matrix(a)
m2 = Matrix(b)
m3 = Matrix(c)

print(m1+m2+m3)  # проверка сложения поэлементно трёх матриц
