
class retta:

    # Attributi di Retta
    

    #Metodo costruttore
    def __init__(self,a, b, c):

        # Attributi di Istanza
        self.a = a
        self.b = b
        self.c = c
       
        
    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n Targa: {self.targa}\n colore: {self.colore}\n assicurazione: {self.assicurazione}\n tipo carburante: {self.tipo_carburante}' 
    
giovanni = auto("giovanni","ford","fiesta","AX 123 XA", "rosso", "benzina verde")

marco = auto("marco","fiat","Bravo","FB 104 HE", "verde", "gpl")

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
