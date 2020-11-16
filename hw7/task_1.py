# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix):
        # проверяем, что все подмассивы имеют одинаковое количество элементов
        if not all([len(matrix[0]) == len(matrix[i]) for i in range(1, len(matrix))]):
            raise ValueError('Matrix have different quantity of elements in vectors')
        self.__matrix = matrix

    def __str__(self):
        matrix_rows = []
        for row in self.__matrix:
            matrix_rows.append(' '.join(f'{x:>2}' for x in row))
        return '\n'.join(matrix_rows)

    def __add__(self, other):
        # проверяем, что матрицы имеют одинаковую размерность
        if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
            res_arrays = []
            for i in range(len(self.__matrix)):
                res_arrays.append([other.__matrix[i][j] + self.__matrix[i][j] for j in range(len(self.__matrix[0]))])
            return Matrix(res_arrays)
        else:
            raise ValueError('Value error: matrices have different quantity of elements')


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1)
print(m1 + m2)

m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m4 = Matrix([[1, 2], [4, 5]])
print(m3 + m4)
