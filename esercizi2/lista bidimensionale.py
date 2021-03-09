#lista bidimensionale

from random import randint
Riga = 3
Colonne = 3

lista = []
for l in range(Riga):
    Colonna = [randint(1,100), randint(1,100), randint(1,100)]
    lista.append(Colonna)

print(lista)
for l in range(len(lista)):
    print(lista[l])
selezione_Riga = int(input("quale riga vuoi che ti mostro? ")) - 1


print(f"L'elemento selezionato è {lista[selezione_Riga]}")
