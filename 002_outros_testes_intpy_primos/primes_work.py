from math import sqrt
import sys

primos_dir = "../Arquivos/primos.txt"

def add_prime(n):
    with open(primos_dir, "a") as f:
        f.writelines('\n'.join(["", str(n)]))


def init():
    lista = []
    with open(primos_dir, "r")as f:
        for line in f:
            lista.append(int(line))
    return lista


def is_prime(n):
    limite = int(sqrt(n)) + 2
    with open(primos_dir, "r") as f:
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


def get_next(lista):
    atual = lista[-1]
    while True:
        atual += 1
        limite = int(sqrt(atual))+2
        eh = 1
        for primo in lista:
            if atual%primo == 0:
                eh = 0
                break
            if primo >= limite:
                break
        if eh:
            add_prime(atual)
            lista.append(atual)
            break


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
    atual = 0
    print(atual)
    lista = init()
    print(lista[-1])
    while True:
        get_next(lista)




