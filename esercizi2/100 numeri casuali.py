
#100 numeri casuali 

from random import randint

lista = 100

with open("testo.txt", "w") as f:
    for a in range(lista):
        f.write(str(randint(1,100)) + "\n")

with open("testo.txt", "r") as f:
    for line in f: print(line, end="")
