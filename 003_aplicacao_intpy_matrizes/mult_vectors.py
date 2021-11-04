#implementação utilizando granulosidade vetor e matriz
import sys
sys.path.append("C:/Code/Repos/pibiti")

from intpy.intpy import initialize_intpy, deterministic
from packs.main import *

import time

@deterministic
def prod_int(a, b):
    n = len(a)
    prod = 0
    for i in range(n):
        prod += a[i]*b[i]
    return prod


@deterministic
def mult(A, B):
    B = B.T()
    matrix = []

    for i in range(A.size[0]):
        line = []
        for j in range(A.size[1]):
            line.append(prod_int(A.matrix[i], B.matrix[j]))
        matrix.append(line)

    return Matrix(matrix=matrix)


@initialize_intpy(__file__)
def main(A, B):
    C = mult(A, B)

if __name__ == "__main__":
    n = int(sys.argv[1])
    A = Matrix(file="{}_1_file.txt".format(n))
    B = Matrix(file="{}_2_file.txt".format(n))

    start = time.perf_counter()
    main(A, B)
    print(time.perf_counter()-start)
