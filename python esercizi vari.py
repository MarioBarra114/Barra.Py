#ESERCIZI VARI

nome = input('Inserisci il tuo nome: ')

print (nome)
#Chiedi all'utente del programma il suo nome e restituiscilo come output.


cognome = input('Inserisci il tuo cognome:')
print (nome, cognome) 

lunghezza_nome = len (nome)
print ('il tuo nome è composto da ',lunghezza_nome, 'caratteri')


lunghezza_cognome = len (cognome )
print ('il tuo cognome è composto da ',lunghezza_cognome, 'caratteri')

#prendi in input due numeri e restituiscili ordinati prima il più piccolo poi  il più grande
n1 = input ('inserisci il primo numero:')
n2 = input ('inserisci il secondo numero:')
a = [n1, n2]
a.sort()
print(a)


#colorepreferito

colore_preferito = input ('inserisci il tuo colore preferito:')

if colore_preferito == 'rosso':
    print ('bello')
elif colore_preferito =='Rosso':
    print ('bello')
elif colore_preferito == 'ROSSO':
    print ('bello')
else: print ('non mi piace')

#stampa 3 volte il nome
seq = [1, 2, 3]
for i in seq :
    print (nome )

#Chiedi all'utente il suo nome e restituisci in output tutte le lettere del nome, una alla volta

s = nome
for x in s:
    print(x)



#variabile frutta

frutta = 'pera, albicocca, mela e banana'

print (frutta[17:21])

#4elementi

elementi = 'zaino, astuccio, penna, libro'
print(elementi)
print ('scegli un elemento e scrivilo')
elemento_scelto =input('Inserisci elemento')
print (elemento_scelto)

#lista di 5 elementi

seq2 = [1]
elementi2 = ['tavolo, bicchiere,tovagliolo, bottiglia,acqua']
for i in seq2 :
    print (elementi2)


#lista 10 elementi con metodo sort

elementi3 = 'giubbino,sciarpa,guanto,cappello,libro,treno,metropolitana, aereo,automobile,computer'


lista = ['giubbino','sciarpa','guanto','cappello', 'libro', 'treno','metropolitana','aereo', 'automobile','computer']
lista.sort()
print(lista)


#filejson 10 libri
import json
data = {'libri': [{'promessi sposi': 'Manzoni', 'Lucia': 'Romanzo storico'},
                  {'Odissea ': 'Omero', 'poema': ' Ulisse'},
                  {'Eneide':' Virgilio', 'Poema':'Enea'},
                  {'Uno, nessuno e centomila ':' Pirandello', 'Romanzo ':'monologo'},
                  {'Malavoglia':' Verga', 'Romanzo':'lo zio Crocifisso'},
                  {'It':' Spephen King ', 'Horror':'it'},
                  {'Shining ':' Stephen KIng ', 'horror':'Danny Torrance'},
                  {'Io robot':' Isaac Asimov', 'Antologia':'Susan calvin'},
                  {'Viaggio al centro della Terra ':' Jules Verne ', 'Romanzo  ':'il professor Lidenbrock'},
                  {'Romeo e Giuliett':'Shakespeare', 'tragedia':'Giulietta'}]}
with open("output.json", "w") as outfile:
    json.dump(data, outfile)

print (data)
