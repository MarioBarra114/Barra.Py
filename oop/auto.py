'''
Python3
Programmazione ad oggetti
'''

class auto:

    # Attributi di Classe
    garanzia = 1
    assicurazione = True
    parcoAuto = 0

    #Metodo costruttore
    def __init__(self,proprietario, marca, modello, cilidrata, cavalli, colore, tipo_carburante):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilidrata
        self.cavalli = cavalli
        self.colore = colore
        self.tipo_carburante = tipo_carburante
        
        auto.parcoAuto +=1

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n Cilindrata: {self.cilindrata}\n Cavalli: {self.cavalli}\n colore: {self.colore}\n assicurazione: {self.assicurazione}\n tipo carburante: {self.tipo_carburante}' 
    
giovanni = auto("giovanni","ford","fiesta",1500, 160, "rosso", "benzina verde")

marco = auto("marco","fiat","Bravo",2500, 200, "verde", "gpl")

print("Il tipo di variabile costruita è:")
print(giovanni)
print(marco)

print("\nLa singola scheda è:")
print (giovanni.scheda())
print (marco.scheda())
print("\nauto totali: ",auto.parcoAuto)

print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(giovanni.__dict__)
print(marco.__dict__)
