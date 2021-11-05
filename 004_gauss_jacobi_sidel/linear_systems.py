import sys
sys.path.append("C:/Code/Repos/pibiti")

from packs.main import *

class Sistema:
    """
    A.x = b
    """

    def __init__(self, A, b):
        #check
        if A.size[1] == b.size:
            matrix = []
            for i in range(b.size):
                matrix.append(Vector(vector = A.matrix[i]+[b.vector[i]]))
            self.matrix = matrix
            self.A = A
            self.b = b
            self.solution = None

            if A.size[0] == A.size[1]:
                self.type = 1
            elif A.size[0] > A.size[1]:
                self.type = 2
            else:
                self.type = 3
        else:
            self.matrix = None
            self.A = None
            self.b = None
            self.solution = None
            self.type = None

    def show(self, elements=100000):
        n = int(log10(elements)) + 1
        for i in range(len(self.matrix)):
            self.matrix[i].show()
        print("")
    

    def gauss_jordan(self):
        S = self

        pivo_cols = 0

        for line_pivo in range(len(S.matrix)):

            for i in range(line_pivo, len(S.matrix)):
                if S.matrix[i].vector[pivo_cols] != 0 and i==line_pivo:
                    break

                elif S.matrix[i].vector[pivo_cols] != 0:
                    S.matrix[line_pivo], S.matrix[i] = S.matrix[i], S.matrix[line_pivo]
                    break

            for i in range(line_pivo, len(S.matrix)):
                if S.matrix[i].vector[pivo_cols] != 0:
                    fator = S.matrix[i].vector[pivo_cols]
                    S.matrix[i].multi(1/fator)
                    if i != line_pivo: S.matrix[i] = S.matrix[i] - S.matrix[line_pivo]

            pivo_cols += 1

        pivo_cols -= 1
        for line in range(len(S.matrix)-1, -1, -1):
            for i in range(line-1, -1, -1):
                now = S.matrix[i].vector[pivo_cols]
                if now != 0:
                    S.matrix[i].vector[pivo_cols] = 0
                    S.matrix[i].vector[-1] -= S.matrix[line].vector[-1]*now
            pivo_cols -= 1
        answer = []
        for i in range(len(S.matrix)):
            answer.append(S.matrix[i].vector[-1])

        self.solution = Vector(vector = answer)


    def gauss_jacobi(self):
        pass

if __name__ == '__main__':
    A = [[1, 1, 1], [1, 2, 2], [2, 1, 3]]
    A = Matrix(matrix = A)
    b = [6, 9, 11]
    b = Vector(vector = b)
    S = Sistema(A, b)
    S.show()



