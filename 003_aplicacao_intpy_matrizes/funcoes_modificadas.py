from random import randint

class Matrix:

    def create(n, element_range):
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                a = randint(0, element_range)
                matrix[i].append(a)

        return matrix

    def __init__(self, file_name = ""):
        self.matriz = 