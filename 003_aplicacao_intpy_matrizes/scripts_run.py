from os import system

def intpy_test(ds = "list", gra = "mat"):
    files = {   "mat":["m_nc.dat", "m_ic.dat", "m_fc.dat"],
                "vec":["v_nc.dat", "v_ic.dat", "v_fc.dat"],
                "mat_vec":["mv_nc.dat", "mv_ic.dat", "mv_fc.dat"]}

    struct = {"list":"list", "my":"my", "numpy":"numpy"}

    python_file = ds + "_" + gra + ".py"

    ran = 100
    size = 200

    file = ["results/" + struct[ds] + "_" + files[gra][0], "results/" + struct[ds] + "_" + files[gra][1], "results/" + struct[ds] + "_" + files[gra][2]]

    print("---------------------------------")
    print(f"DataStruct: {ds}")
    print(f"Granularity: {gra}")
    print("Cleaning up cache")
    system("rmdir  /s /q .intpy")
    system("mkdir results")
    system(f"rmdir /s /q {file[0]}")
    system(f"rmdir /s /q {file[1]}")
    system(f"rmdir /s /q {file[2]}")
    print("---------------------------------")

    print("--no-cache execution")
    file = "results/" + struct[ds] + "_" + files[gra][0]
    for i in range(1, ran):
        system(f"python {python_file} {size} {i} {i+1} -v v027x -s pickle --no-cache >> {file}")
    print("done!\n")

    print("only intra cache")
    file = "results/" + struct[ds] + "_" + files[gra][1]
    for i in range(1, ran):
        system(f"python {python_file} {size} {i} {i+1} -v v027x -s pickle >> {file}")
        system("rmdir /s /q .intpy")
    print("done!\n")

    print("full cache")
    file = "results/" + struct[ds] + "_" + files[gra][2]
    for i in range(1, ran):
        system(f"python {python_file} {size} {i} {i+1} -v v027x -s pickle >> {file}")
    print("done!")

    system("rmdir /s /q .intpy")


if __name__ == "__main__":
    intpy_test()
    intpy_test(gra="mat_vec")
    intpy_test(gra="vec")
    pass

