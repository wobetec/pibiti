from os import system
import sys
sys.path.append("../")

from packs.main_list import *

from random import randint

def change_line(file_one, line_one, file_two, line_two):
    A = Matrix(file = file_one)
    B = Matrix(file = file_two)

    print(line_one, "+", line_two)
    A.matrix[line_one] = B.matrix[line_two]
    A.save_txt(file_one)


def intpy_test(ds = "list", gra = "mat"):
    files = {   "mat":["m_nc.dat", "m_ic.dat", "m_fc.dat"],
                "vec":["v_nc.dat", "v_ic.dat", "v_fc.dat"],
                "mat_vec":["mv_nc.dat", "mv_ic.dat", "mv_fc.dat"]}

    struct = {"list":"list", "my":"my", "numpy":"numpy"}

    python_file = ds + "_" + gra + ".py"

    ran = 100

    file = ["results/" + struct[ds] + "_" + files[gra][0], "results/" + struct[ds] + "_" + files[gra][1], "results/" + struct[ds] + "_" + files[gra][2]]

    print("---------------------------------")
    print("Change lines test")
    print(f"DataStruct: {ds}")
    print(f"Granularity: {gra}")
    print("Cleaning up cache")
    system("rmdir  /s /q .intpy")
    system("mkdir results")
    system(f"rmdir /s /q {file[0]}")
    system(f"rmdir /s /q {file[1]}")
    system(f"rmdir /s /q {file[2]}")
    print("---------------------------------")

    lines_origin = "200_3_file.txt"
    matrix1 = "200_1_file.txt"
    C = Matrix(file = matrix1)
    matrix2 = "200_2_file.txt"
    """
    print("--no-cache execution")
    file = "results/" + struct[ds] + "_" + files[gra][0]
    for i in range(1, ran):
        system(f"python {python_file} 200 1 2 -v v027x -s pickle --no-cache >> {file}")
        a, b = randint(0, 199), randint(0, 199)
        change_line(matrix1, a, lines_origin, b)
    C.save_txt(matrix1)
    print("done!\n")
    """

    if gra == "mat":
        print("only intra cache")
        file = "results/" + struct[ds] + "_" + files[gra][1]
        for i in range(1, ran):
            system(f"python {python_file} 200 1 2 -v v027x -s pickle >> {file}")
            a, b = randint(0, 199), randint(0, 199)
            change_line(matrix1, a, lines_origin, b)
            system("rmdir /s /q .intpy")
        C.save_txt(matrix1)
        print("done!\n")
    

    print("full cache")
    file = "results/" + struct[ds] + "_" + files[gra][2]
    for i in range(1, ran):
        system(f"python {python_file} 200 1 2 -v v027x -s pickle >> {file}")
        a, b = randint(0, 199), randint(0, 199)
        change_line(matrix1, a, lines_origin, b)
    C.save_txt(matrix1)
    print("done!")


    system("rmdir /s /q .intpy")


if __name__ == "__main__":
    #intpy_test()
    #intpy_test(gra="mat_vec")
    intpy_test(gra="vec")
    pass
