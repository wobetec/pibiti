#fibonacci_recursive.py

import time
import sys

from intpy.intpy import initialize_intpy, deterministic

from random import randint

def vec(n):
    vetor = [randint(0, 1) for i in range(n)]
    return vetor


@deterministic
def prod_int(a, b):
    prod = 0
    for i in range(len(a)):
        prod += a[i]*b[i]
    return prod


@initialize_intpy(__file__)
def main(a, b):
    print(a, "  ", b)
    print(prod_int(a, b))


if __name__ == "__main__":
    n = int(sys.argv[1])
    start = time.perf_counter()
    a = vec(n)
    b = vec(n)
    main(a, b)
    print(time.perf_counter()-start)
