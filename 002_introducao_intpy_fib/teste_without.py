
lista = [2, 3]
n = 1000
for i in range(5, n+1):
    primo = 1
    for j in lista:
        if i%j == 0 :
            primo = 0
            break
    if primo:
        lista.append(i)

print(lista)
