
lista_settimana = ['lun','mar','mer','gio','ven','sab','dom']
print(lista_settimana[1]) #voglio martedì
print(lista_settimana[-1]) #voglio domenica
print(len(lista_settimana)) #len per contare lunghezza lista , print per stampare. restituisce 7

citta = ['napoli','firenze','roma','bari','torino','palermo']
print(citta[0]) #stampo il primo elemento
print(citta[-2]) #stampo il penultimo

frutta = ['mela', 'pera', 'banana', 'pomodoro', 'anguria']
print(frutta[4]) #stampo l'ultimo elemento senza usare negativi
ultimo = len(frutta)-1 #alloco una variabile con nlist-1
print(frutta[ultimo]) #printo puntando all'ultimo elemento con la variabile ultimo
print(frutta[len(frutta)-1]) #senza usare una variabile, faccio tutto qui



lista_numeri = [1,2,3,4,5,6]
k = int(input("digita un numero da 0 a 5 "))
if 0 <= k < len(lista_numeri):
    print(f"l'elemento in posizione {k} è: ", lista_numeri[k])
else:
    print(f"errore indice non valido")
    

#slicing
#da una list ne prendiamo dei sottoinsiemi 
#sintassi : nomelista[start:stop:step]
#lo step è opzionale, se non messo è di default 1
#lo start anche si può omettere nomelist[:5] python userà il primo elemento della lista di default
#se non mettiamo l'end, python da' di default l'ultimo elemento della lista
#se non metto niente manda tutta la lista, metto solo i due punti
#se metto così [::-1] restituisce la lista al contrario

numeri = [0,1,2,3,4,5,6,7,8,9]
print(numeri[2:5])

lista_settimana = ['lun','mar','mer','gio','ven','sab','dom']
#voglio stampare dal terzo al quinto quindi da mer a ven
print(lista_settimana[2:5])
#vogli stampare da lunedì a venerdì
print(lista_settimana[:5])
#senza mettere lo stop
print(lista_settimana[5:])
#senza nulla stampa tutto
print(lista_settimana[::])
#la vogliamo al contrario
print(lista_settimana[::-1])


#crea una lista con i numeri da 1 a 9
#stampa dalla 3° posizione alla 6° escluso

numeri = [0,1,2,3,4,5,6,7,8,9]
print(numeri[2:6])

lista_settimana = ['lun','mar','mer','gio','ven','sab','dom']
print(lista_settimana[::-1])

#funzione range()
#usata per generare una sequenza di numeri interi
#sintassi: range(start,stop,step) 

#voglio una lista di 100 interi
#print(list(range(100)))

#voglio una lista fino a 100 interi da 50
#print(list(range(50,101,2)))

#lista da 5 a 15 escluso
#stampa lista e lunghezza
numeri = (list(range(5,15)))
print(numeri)
print(len(numeri))


#scorrere una lista col ciclo for e range
#------------metodo con indice
giorni = ['lun','mar','mer']
lunghezza = len(giorni)
lista_indici = list(range(0,lunghezza))
print(f"Lista originale {giorni}")
print(f"lsita indici {lista_indici}")
for indice in lista_indici:
    print(indice)
    print(giorni[indice])

#------------metodo con l'elemento
giorni = ['lun','mar','mer']
for elemento in giorni:
    print(elemento)
 
#esercizio
materie = ['ita','mat','sto','geo','ing']
voti =[8,6,5,9,8,]
lung_materie = len(materie)
lung_voto = len(voti)
print(f"le materie sono {lung_materie}, i voti sono {lung_materie}")
lista_indici = list(range(0,lung_materie))
print(f"gli indici sono {lista_indici}")
for indice in lista_indici:
        print(f"{materie[indice]} : {voti[indice]}")
        
      
#possiamo usare il for col range per chiedere di inserire numeri in una lista
n = int(input("quanti numeri vuoi inserire?"))
numerilist = []

for i  in range(n):
    num = int(input("inserisci un numero"))
    numerilist.append(num)
    
print(numerilist)

#posso anche mettere elementi a caso se non dico che devono essere int