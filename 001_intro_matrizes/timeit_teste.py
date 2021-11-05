import sys
sys.path.append("C:/Code/Repos/pibiti")
import timeit
from packs.main import *

begin = 90
size = 100
times = 10

M = Matrix

def f_create():
    for i in range(begin, size):
        M.generate("{}_1_file.txt".format(i), i)
        M.generate("{}_2_file.txt".format(i), i)

def f_mul():
    for i in range(begin, size):
        A = M(file = "{}_1_file.txt".format(i))
        B = M(file = "{}_2_file.txt".format(i))
        C = A * B
        #C.save_txt("{}_mul_file.txt".format(i))

def f_add():
    for i in range(begin, size):
        A = M(file = "{}_1_file.txt".format(i))
        B = M(file = "{}_2_file.txt".format(i))
        C = A * B
        #C.save_txt("{}_add_file.txt".format(i))

def f_sub():
    for i in range(begin, size):
        A = M(file = "{}_1_file.txt".format(i))
        B = M(file = "{}_2_file.txt".format(i))
        C = A * B
        #C.save_txt("{}_sub_file.txt".format(i))


print("Creation = ", end="")
print(timeit.timeit(f_create, number = times)/times)

print("Multiply = ", end="")
print(timeit.timeit(f_mul, number = times)/times)

print("Add = ", end="")
print(timeit.timeit(f_add, number = times)/times)

print("Sub = ", end="")
print(timeit.timeit(f_sub, number = times)/times)
