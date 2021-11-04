import sys
sys.path.append("C:/Code/Repos/pibiti")

from intpy.intpy import initialize_intpy, deterministic

import time
from primes_work import *


lista = init()


def find_min_fac(n):
    for i in lista:
        if n%i ==0:
            return i


@deterministic
def factory(n):
    lista = []
    a = find_min_fac(n)
    n = int(n/a)
    lista.append(a)
    lista = lista + factory(n)

    return lista


@initialize_intpy(__file__)
def main(n):
    print(factory(n))


if __name__ == "__main__":
    n = int(sys.argv[1])
    start = time.perf_counter()
    main(n)
    print(time.perf_counter()-start)


