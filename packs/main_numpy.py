from math import log10
from random import randint
import numpy as np

mat_dir = "../Arquivos/matrizes/"


class Matrix:

    def read_file(file_name):
        filename = mat_dir + file_name

        matrix = []
        with open(filename, "r") as f:

            for line in f:
                linha = [int(x) for x in line.split()]
                matrix.append(linha)

        return np.array(matrix)


    def create(n, m=0, elements=100):
        matrix = []

        for i in range(n):
            line = [randint(0, elements) for j in range(m if m != 0 else n)]
            matrix.append(line)

        return np.array(matrix)


    def __init__(self, n=0, m=0, file=None, matrix=None, range=100):
        #Criar matriz
        if n != 0: 
            self.matrix = Matrix.create(n, m = m, elements = range)
            self.size = self.matrix.shape

        #File
        elif file != None: 
            self.matrix = Matrix.read_file(file)
            self.size = self.matrix.shape

        #matriz de matrix
        elif matrix.any():
            self.matrix = matrix
            self.size = self.matrix.shape

        #Gera matrix vazia
        else:
            self.matrix = None
            self.size = None


    def __add__(self, other):
        matrix = self.matrix + other.matrix
        return Matrix(matrix = matrix)


    def __sub__(self, other):
        matrix = self.matrix - other.matrix
        return Matrix(matrix = matrix)


    def T(self):
        matrix = self.matrix.transpose()
        return Matrix(matrix = matrix)


    def __mul__(self, other):
        matrix = self.matrix.dot(other.matrix)
        return Matrix(matrix = matrix)
        """
        
        """


    def show(self, elements=100000):
        n = int(log10(elements)) + 1
        for line in self.matrix:
            for i in line:
                print(f"{i}".rjust(n," "), end="")
            print("")


    def save_txt(self, file_name):
        prefix = mat_dir
        filename = prefix + file_name

        with open(filename, "w") as f:
            for line in self.matrix:
                f.write(" ".join(str(a) for a in line))
                f.write("\n")


    def generate(file_name, n, m=0,  elements=100):
        matrix = Matrix(n=n, m=m, range=elements)
        try:
            matrix.save_txt(file_name)
        except:
            print("Generation Erro")


if __name__ == "__main__":
    A = Matrix(file="3_1_file.txt")
    B = Matrix(file="3_2_file.txt")
    C = A*B
    C.show()
    pass

