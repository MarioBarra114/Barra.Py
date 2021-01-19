from guizero import *

app = App(title= "prodotto intermedio python" )
message = Text(app, text= " Questo programma permette di disegnare  un grafico a partire dal tuo file.")
               

message = Text(app, text= "inserisci il nome del file:" )

file = TextBox(app, text= "")

app.display()

print (file)

