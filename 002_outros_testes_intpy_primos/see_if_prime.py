from math import sqrt
import sys

def is_prime(n):
    limite = int(sqrt(n)) + 2
    with open("primos.txt", "r") as f:
        eh = 1
        for line in f:
            prime = int(line)
            if n % prime == 0:
                eh = 0
                break
            if prime > limite:
                break
        if eh:
            return True
        else:
            return False

if __name__ == "__main__":
    n = int(sys.argv[1])
    if is_prime(n):
        print("Eh primo")
    else:
        print("N eh primo")


