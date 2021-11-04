#fibonacci_recursive.py

import time
import sys
import main_03

from intpy.intpy import initialize_intpy, deterministic


@deterministic
def function(n):
    A = main_03.read_file(("{}_1_file.txt".format(n)))
    B = main_03.read_file("{}_2_file.txt".format(n), length=n)
    C = [[] for i in range(n)]

    for i in range(n):#A
        for j in range(n):#B
            a = C[i]
            a.append(main_03.prod_int(A[i], B[j], n))
    
    return C


@initialize_intpy(__file__)
def main(n):
    if function(n) != None:
        print("Done")

if __name__ == "__main__":
    n = int(sys.argv[1])
    start = time.perf_counter()
    main(n)
    print(time.perf_counter()-start)
