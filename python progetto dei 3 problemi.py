def equazione(a,b):
	return(b*(-1)/a)

print("Calcolo equazione di primo grado")


a=int(input("inserisci il coefficiente della x "))
b=int(input("inserisci il termine noto "))




print(equazione(a,b))



def massimo(a1,b1,c1):
    return(max(a1,b1,c1))

print("calcolo il massimo di 3 numeri")
a1=int(input("inserisci il primo numero: "))
b1=int(input("inserisci il secondo numero: "))
c1=int(input("inserisci il terzo numero: "))

print(massimo(a1,b1,c1))


def swap(x,y):
    return y,x


print("inverto le due variabili")
x=int(input("inserisci la prima variabile:"))
y=int(input("inserisci la seconda variabile:"))

print(swap(x,y))
