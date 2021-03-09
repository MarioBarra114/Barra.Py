#lista di 5 numeri 

print("Inserisci 5 numeri e te li mostro in ordine inverso : ")
lista = []
for x in range(5):
    numero = input()

    lista.append(numero)

print(list(reversed(lista)))
