from math import log10
from random import randint

mat_dir = "../Arquivos/matrizes/"
vec_dir = "../Arquivos/vectors/"


class Matrix:


    def read_file(file_name):
        filename = mat_dir + file_name

        matrix = []
        with open(filename, "r") as f:

            for line in f:
                linha = [int(x) for x in line.split()]
                matrix.append(linha)

        return matrix


    def create(n, m=0, elements=100):
        matrix = []

        for i in range(n):
            line = [randint(0, elements) for j in range(m if m != 0 else n)]
            matrix.append(line)

        return matrix


    def __init__(self, n=0, m=0, file=None, matrix=None, range=100):
        if n != 0:
            self.matrix = Matrix.create(n, m = m, elements = range)
            self.size = (n, m if m!=0 else n)

        elif file != None:
            self.matrix = Matrix.read_file(file)
            self.size = (len(self.matrix), len(self.matrix[0]))

        elif matrix != None:
            self.matrix = matrix
            self.size = (len(matrix), len(matrix[0]))

        else:
            self.matrix = None
            self.size = None


    def __add__(self, other):
        #Do
        matrix = []
        for i in range(self.size[0]):
            line = []
            for j in range(self.size[1]):
                line.append(self.matrix[i][j] + other.matrix[i][j])
            matrix.append(line)

        return Matrix(matrix=matrix)


    def __sub__(self, other):
        #Do
        matrix = []
        for i in range(self.size[0]):
            line = []
            for j in range(self.size[1]):
                line.append(self.matrix[i][j] - other.matrix[i][j])
            matrix.append(line)

        return Matrix(matrix=matrix)


    def T(self):
        matrix = []

        for i in range(self.size[1]):
            col = [self.matrix[j][i] for j in range(self.size[0])]
            matrix.append(col)
        
        return Matrix(matrix=matrix)


    def prod_int(a, b, n):
        prod = 0
        for i in range(n):
            prod += a[i]*b[i]
        return prod


    def __mul__(self, other):
        #Do
        B = other.T()
        matrix = []

        for i in range(self.size[0]):
            line = []
            for j in range(self.size[1]):
                line.append(Matrix.prod_int(self.matrix[i], B.matrix[j], self.size[1]))
            matrix.append(line)

        return Matrix(matrix=matrix)


    def show(self, elements=100000):
        n = int(log10(elements)) + 1
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                print(f"{self.matrix[i][j]}".rjust(n," "), end="")
            print("")


    def save_txt(self, file_name):
        prefix = mat_dir
        filename = prefix + file_name

        with open(filename, "w") as f:
            for i in range(self.size[0]):
                f.write(" ".join(str(a) for a in self.matrix[i]))
                f.write("\n")


    def generate(file_name, n, m=0,  elements=100):
        matrix = Matrix(n=n, m=m, range=elements)
        try:
            matrix.save_txt(file_name)
        except:
            print("Generation Erro")


class Vector:


    def read_file(file_name):
        filename = vec_dir + file_name

        vector = []
        with open(filename, "r") as f:
            for line in f:
                vector = line.split(" ")

        return vector


    def create(n, elements=100):
        vector = [randint(0, elements) for j in range(n)]

        return vector


    def __init__(self, n=0, file=None, vector=None, range=100):
        if n != 0:
            self.vector = Vector.create(n, elements = range)
            self.size = n

        elif file != None:
            self.vector = Vector.read_file(file)
            self.size = len(self.vector)

        elif vector != None:
            self.vector = vector
            self.size = len(vector)

        else:
            self.vector = None
            self.size = None


    def __add__(self, other):
        vector = []
        for i in range(self.size):
            vector.append(self.vector[i] + other.vector[i])

        return Vector(vector=vector)


    def __sub__(self, other):
        vector = []
        for i in range(self.size):
            vector.append(self.vector[i] - other.vector[i])

        return Vector(vector=vector)


    def __mul__(self, other):
        prod = 0
        for i in range(self.size):
            prod += self.vector[i] * other.vector[i]
        return prod


    def show(self, elements=100000):
        n = int(log10(elements)) + 1
        for i in range(self.size):
            print(f"{self.vector[i]}".rjust(n," "), end="")
        print("")

    def save_txt(self, file_name):
        prefix = vec_dir
        filename = prefix + file_name

        with open(filename, "w") as f:
            f.write(" ".join(str(a) for a in self.vector))


    def generate(file_name, n, elements=100):
        vector = Vector(n=n, range=elements)
        try:
            vector.save_txt(file_name)
        except:
            print("Generation Erro")


if __name__ == "__main__":
    for i in range(2, 101):
        Matrix.generate("{}_1_file.txt".format(i), i)
        Matrix.generate("{}_2_file.txt".format(i), i)
    pass
