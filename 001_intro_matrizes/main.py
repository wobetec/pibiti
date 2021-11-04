from random import randint

mat_dir = "../Arquivos/matrizes/"


def create(n, elements):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            a = randint(0, elements)
            matrix[i].append(a)

    return matrix


def save(file_name, matrix, n):
    prefix = mat_dir
    filename = prefix + file_name

    with open(filename, "w") as f:
        for i in range(n):
            for j in range(n):
                f.write(str(matrix[i][j])+" ")
            f.write("\n")


def generate(filename, n, elements=100):
    matrix = create(n, elements)
    try:
        save(filename, matrix, n)
    except:
        print("Creation Erro")


def read_file(file_name, length=0):

    prefix = mat_dir
    filename = prefix + file_name

    if not length:
        matrix = []
        with open(filename, "r") as f:
            for line in f:
                linha = [int(x) for x in line.split()]
                matrix.append(linha)
    else:
        matrix = [[] for i in range(length)]
        with open(filename, "r") as f:
            for line in f:
                linha = [int(x) for x in line.split()]
                for i in range(length):
                    matrix[i].append(linha[i])

    return matrix

def add(A_file, B_file, n):
    A = read_file(A_file)
    B = read_file(B_file)
    C = [[] for i in range(n)]
    for i in range(n):
        a, b = A[i], B[i]
        for j in range(n):
            C[i].append(a[j]+b[j])
    
    return C

def sub(A_file, B_file, n):
    A = read_file(A_file)
    B = read_file(B_file)
    C = [[] for i in range(n)]
    for i in range(n):
        a, b = A[i], B[i]
        for j in range(n):
            C[i].append(a[j]-b[j])
    
    return C

def prod_int(a, b, n):
    prod = 0
    for i in range(n):
        prod += a[i]*b[i]
    return prod


def multiply(A_file, B_file, n):
    A = read_file(A_file)
    B = read_file(B_file, length=n)
    C = [[] for i in range(n)]

    for i in range(n):#A
        for j in range(n):#B
            C[i].append(prod_int(A[i], B[j], n))
    
    return C


if __name__ == "__main__":
    generate("mat1.txt", 3)
    generate("mat2.txt", 3)

    A = read_file("mat1.txt")
    print(A)
    B = read_file("mat2.txt")
    print(B)

    C = add("mat1.txt", "mat2.txt", 3)
    print(C)
    





