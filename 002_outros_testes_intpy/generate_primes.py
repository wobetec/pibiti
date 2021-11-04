from math import sqrt

def add_prime(n,):
    with open("primos.txt", "a") as f:
        f.writelines('\n'.join(["", str(n)]))


def init():
    lista = []
    with open("primos.txt", "r")as f:
        for line in f:
            lista.append(int(line))
    return lista


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


def get_next(lista):
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

if __name__ == "__main__":
    atual = 0
    with open("primos.txt", "r") as f:
        for line in f:

            
while True:
    get_next(lista)




