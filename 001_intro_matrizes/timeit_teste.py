import timeit
import main

size = 100
times = 10

def f0():
    for i in range(2, size):
        main.generate("{}_1_file.txt".format(i), i)
        main.generate("{}_2_file.txt".format(i), i)

def f3():
    for i in range(2, size):
        C = main.multiply("{}_1_file.txt".format(i), "{}_2_file.txt".format(i), i)
        main.save("{}_3_file.txt".format(i), C, i)

def f3_add():
    for i in range(2, size):
        C = main.add("{}_1_file.txt".format(i), "{}_2_file.txt".format(i), i)
        main.save("{}_3_add_file.txt".format(i), C, i)

def f3_sub():
    for i in range(2, size):
        C = main.sub("{}_1_file.txt".format(i), "{}_2_file.txt".format(i), i)
        main.save("{}_3_sub_file.txt".format(i), C, i)


print("Creation = ", end="")
print(timeit.timeit(f0, number = times)/times)

print("03 = ", end="")
print(timeit.timeit(f3, number = times)/times)

print("03 Soma = ", end="")
print(timeit.timeit(f3_add, number = times)/times)

print("03 Subtracao = ", end="")
print(timeit.timeit(f3_sub, number = times)/times)
