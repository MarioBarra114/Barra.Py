#quante volte si ripete il numero che hai scelto?


from random import randint
lista = []

for x in range(5):
    numero=randint(1,8)
    lista.append(numero)

print(lista)

Numero = input("Scegli un numero tra quelli che ti ho mostrato , e io ti dirò quante volte compare :")
conta = 0
for c in lista:
    if (Numero == str(c)):
        conta += 1

print("Il numero ",Numero," risulta ",conta," volte")
