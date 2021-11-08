#implementado a multiplicação com granulosidade matriz
import sys
sys.path.append("../packs/")

from intpy.intpy import initialize_intpy, deterministic
from main_list import *

import time


@deterministic
def mult(A, B):
    B = B.T()
    matrix = []

    for i in range(A.size[0]):
        line = []
        for j in range(A.size[1]):
            line.append(Matrix.inner_product(A.matrix[i], B.matrix[j]))
        matrix.append(line)

    return Matrix(matrix=matrix)


@initialize_intpy(__file__)
def main(A, B):
    C = mult(A, B)
    C.show()


if __name__ == "__main__":
    n, a, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    A = Matrix(file="{}_{}_file.txt".format(n, a))
    B = Matrix(file="{}_{}_file.txt".format(n, b))

    start = time.perf_counter()
    main(A, B)
    print(time.perf_counter()-start)

