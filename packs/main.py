from math import log10
from random import randint

mat_dir = "../Arquivos/matrizes/"


class Matrix:

    def read_file(file_name):
        filename = mat_dir + file_name

        matrix = []
        with open(filename, "r") as f:

            for line in f:
                linha = [int(x) for x in line.split()]
                matrix.append(Matrix(lista=linha))

        return matrix


    def create(n, m=0, elements=100):
        matrix = []

        for i in range(n):
            line = [randint(0, elements) for j in range(m if m != 0 else n)]
            matrix.append(Matrix(lista=line))

        return matrix


    def __init__(self, n=0, m=0, file=None, matrix=None, lista=None, range=100):
        #Criar matriz
        if n != 0: 
            self.matrix = Matrix.create(n, m = m, elements = range)
            self.size = (n, m if m!=0 else n)

        #File
        elif file != None: 
            self.matrix = Matrix.read_file(file)
            self.size = (len(self.matrix), len(self.matrix[0].matrix))

        #matriz de matrix
        elif matrix != None:
            self.matrix = matrix
            self.size = (len(matrix), matrix[0].size[1])

        #lista de inteiros
        elif lista != None:
            self.matrix = lista
            self.size = (1, len(lista))

        #Gera matrix vazia
        else:
            self.matrix = None
            self.size = None


    def __add__(self, other):

        if self.size[0] == 1:
            line = []
            for i in range(self.size[1]):
                a, b = self.matrix[i], other.matrix[i]
                line.append(a + b)
            return Matrix(lista = line)

        else:
            matrix = []
            for i in range(self.size[0]):
                u, v = self.matrix[i], other.matrix[i]
                matrix.append(u + v)
            return Matrix(matrix = matrix)


    def __sub__(self, other):
        if self.size[0] == 1:
            line = []
            for i in range(self.size[1]):
                a, b = self.matrix[i], other.matrix[i]
                line.append(a - b)
            return Matrix(lista = line)

        else:
            matrix = []
            for i in range(self.size[0]):
                u, v = self.matrix[i], other.matrix[i]
                matrix.append(u - v)
            return Matrix(matrix = matrix)


    def T(self):
        matrix = []

        for i in range(self.size[1]):
            col = [self.matrix[j].matrix[i] for j in range(self.size[0])]
            matrix.append(Matrix(lista = col))
        
        return Matrix(matrix=matrix)


    def __mul__(self, other):

        if self.size[0] == 1 and other.size[0] == 1:
            prod = 0
            for i in range(self.size[1]):
                prod += self.matrix[i] * other.matrix[i]
            return prod

        else:
            B = other.T()
            matrix = []

            for i in range(self.size[0]):
                line = []
                for j in range(self.size[1]):
                    line.append(self.matrix[i] * B.matrix[j])
                matrix.append(Matrix(lista = line))

            return Matrix(matrix=matrix)


    def show(self, elements=100000):
        n = int(log10(elements)) + 1
        for line in self.matrix:
            for i in line.matrix:
                print(f"{i}".rjust(n," "), end="")
            print("")


    def save_txt(self, file_name):
        prefix = mat_dir
        filename = prefix + file_name

        with open(filename, "w") as f:
            for line in self.matrix:
                f.write(" ".join(str(a) for a in line.matrix))
                f.write("\n")


    def generate(file_name, n, m=0,  elements=100):
        matrix = Matrix(n=n, m=m, range=elements)
        try:
            matrix.save_txt(file_name)
        except:
            print("Generation Erro")


if __name__ == "__main__":

    pass

