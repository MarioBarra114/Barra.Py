
class retta:

    # Attributi di Retta
    

    #Metodo costruttore
    def __init__(self,a, b, c, m, q, x):

        # Attributi di Istanza
        self.a = a
        self.b = b
        self.c = c
        self.m = -a/b
        self.q = -c/b
        self.x = x
        self.y = -b*x/a-c/a
       
        
    #Metodo di tipo Get
    def esplicita(self):
        return f'\nEquazione in forma esplicita/n"{self.a}"x+"{self.b}"y+"{self.c}"=0' 
    
    def implicita(self):
        return f'\nEquazione in forma implicita/n y="{self.m}"x+"{self.q}"' 
    
     def punti(self):
        return f'\nLa TUPLA è la seguente:"{self.x}" -"{self.y}"' 
    
    
retta1 = retta("giovanni","ford","fiesta","AX 123 XA", "rosso", "benzina verde")

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
