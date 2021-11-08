#implementação utilizando granulosidade vetor e matriz
import sys
sys.path.append("C:/Code/Repos/pibiti")

from intpy.intpy import initialize_intpy, deterministic
from packs.main_my import *

import time


@deterministic
def prod_int(a, b):
    prod = 0
    for i in range(a.size[1]):
        prod += a.matrix[i]*b.matrix[i]
    return prod


@deterministic
def mult(A, B):
    B = B.T()
    matrix = []

    for i in range(A.size[0]):
        line = []
        for j in range(A.size[1]):
            line.append(prod_int(A.matrix[i], B.matrix[j]))
        matrix.append(Matrix(lista = line))

    return Matrix(matrix=matrix)


@initialize_intpy(__file__)
def main(A, B):
    C = mult(A, B)

if __name__ == "__main__":
    n, a, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    A = Matrix(file="{}_{}_file.txt".format(n, a))
    B = Matrix(file="{}_{}_file.txt".format(n, b))

    start = time.perf_counter()
    main(A, B)
    print(time.perf_counter()-start)
