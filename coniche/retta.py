class retta:

    # Attributi di Retta
    

    #Metodo costruttore
    def __init__(self,a, b, c,x):
        

    #Attributi di Istanza

        self.a = a
        self.b = b
        self.c = c
        self.m = -a/b
        self.q = -c/b
        self.x = x
        self.y = -b*x/a-c/a
       
        
    #Metodo di tipo Get
    def implicita(self):
        return f'\nEquazione in forma implicita\n{self.a}x+{self.b}y+{self.c}=0' 
    
    
    def esplicita(self):
        return f'\nEquazione in forma esplicita\ny ={self.m}x+{self.q}' 
    
    
    def tupla(self):
        return f'\nla tupla è : A({self.a},{self.b})' 
    
    
    
retta1 = retta(2,8,-12,7)

print(retta1.implicita())


print(retta1.esplicita())

print(retta1.tupla())


print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(retta1.__dict__)
