#questa funzione fa' quello che vorremmo fare con map
def doppio_lista(lista):
    lista_doppia=[]
    for numero in lista:
        lista_doppia.append(numero*2)
    return lista_doppia

def doppio_elementi(x):
    return x*2
def quadrato_elementi(x):
    return x**2

#map(funzione, lista)
lista_numeri = [1,2,3] #se trasformo questa lista in una matrice non funziona map così strutturato

doppio_lista_numeri = list(map(doppio_elementi, lista_numeri))
print(doppio_lista_numeri)

quadrato_lista_numeri = list(map(quadrato_elementi, lista_numeri))
print(quadrato_lista_numeri)

#per convertire una lista di numeri in una lista di stringhe, si usa map in questo modo
stringa_lista_numeri = list(map(str, lista_numeri))
print(stringa_lista_numeri)

#esercizio
#usando la funzione map() sottrai a tutti gli elementi della lista il numero 2

def sottrai_due(x):
    return x-2

lista_num=list(range(1,6))
lista_sottrazione = list(map(sottrai_due,lista_num))
print(lista_sottrazione)