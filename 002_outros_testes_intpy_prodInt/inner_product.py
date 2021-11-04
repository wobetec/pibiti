import sys
sys.path.append("C:/Code/Repos/pibiti")

from intpy.intpy import initialize_intpy, deterministic
from packs.main import Vector

import time
from random import randint


@deterministic
def prod_int(a, b):
    prod = 0
    for i in range(len(a)):
        prod += a[i]*b[i]
    return prod


@initialize_intpy(__file__)
def main(a, b):
    a.show()
    b.show()
    print(prod_int(a.vector, b.vector))


if __name__ == "__main__":
    n = int(sys.argv[1])
    a = Vector(n=n, range=10)
    b = Vector(n=n, range=10)
    start = time.perf_counter()
    main(a, b)
    print(time.perf_counter()-start)
