#tupla
#collezione ordinata di elementi, simile ad  una lista ma immutabile.
#la indichiamo con le parentesi tonde

tupla = (3.0, -4.5)
x,y = tupla #assegnazione multipla di variabili attraverso una tupla. dobbiamo avere lo stesso numero
print(x)

rgb= ( "#D82929", "#1EBB1E", "#1B7087")
red, green, blue = rgb
print(green)

def operazioni(x,y):
    somma = x+y
    moltiplicazione = x*y
    return somma, moltiplicazione
#opzione A con tupla
risultato = operazioni(5,2)
print(risultato)

#opzione B con spacchettamento
somma, moltiplicazione = operazioni(5,2)
print(somma)
print(moltiplicazione)