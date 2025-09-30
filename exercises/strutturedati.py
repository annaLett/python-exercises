#--------Strutture dati
#esercizio iniziale città-temperatura

citta = ['Torino','Milano','Venezia','Bologna','Firenze','Roma','Napoli','Bari']
temp = []

for indice in citta:
    gradi = int(input(f"inserisci la temperatura di {indice} :"))
    temp.append(gradi)
    
for indice in range(len(citta)):
        print(f"A {citta[indice]} fanno : {temp[indice]} gradi")


#Unionne liste 
lista1 = [1,2,3]
lista2 = [4,5,6]
print(lista1 + lista2) #output [1, 2, 3, 4, 5, 6]
#duplicazione
lista1_doppia = lista1*2 #sto allocando list1 ripetuta due volte
print(lista1_doppia) #output [1, 2, 3, 1, 2, 3]
print(lista1 * 3) #output [1, 2, 3, 1, 2, 3, 1, 2, 3]
#sostituzione elemento lista
lista1[2]=20
print(lista1) #output [1, 2, 20]
#sostituzione più elementi lista
lista2[0:2] = [30, 40] #output [30, 40, 6]
print(lista2)


#Esercizio
frutta1 = ['mela ','banana']
frutta2 = ['arancia','pera']
nuova_lista = frutta1 + frutta2
print(*nuova_lista)
nuova_lista_duplicata = nuova_lista*2
print(*nuova_lista_duplicata)


#Esercizio
numeri =[1,2,3,4,5]
numerii = list(range(1,6))
numeri[1] = 20
print(*numeri)
numeri[3::] = [40,50]
print(*numeri)

#Appartenenza liste
#IN
lista = [1,2,3]
lista.append(4)
print(*lista)
if 4 in lista :
    print("questo numero c'è")

#NOT IN
lista = [1,2,3]
lista.append(4)
print(*lista)
if 5 not in lista :
    print("questo numero non c'è")
    
#PIU' VALORI
lista = [1,2,3]
lista.append(4)
print(*lista)
if 1 and 2 not in lista :
    print("questo numero non c'è")
else:
    print("questo numero c'è")


vacanze = ['mare','montagna','città', 'paese']
#--primo caso controlliamo due elementi
# if ('mare' in vacanze) and ('montagna' in vacanze):
#    print("Si")
#else:
#    print("no")
#--secondo caso, creiamo una lista da controllare che cicliamo
elementi_da_controllare = ['mare', 'montagna','campgna']
for elemento in elementi_da_controllare:
    if elemento in vacanze:
        print(f"l'elemento {elemento} è nella lista vacanze")
    else:
        print(f"l'elemento {elemento} non è nella lista vacanze")

#---------------esercizio
animali = ['gatto','cane','coniglio']
animali.append('criceto')
print(*animali)
#---------------esercizio        
colori = ['rosso','verde','blu']
colori_da_controllare = ['giallo','verde']
for elemento in colori_da_controllare:
    if elemento in colori:
        print(f"il colore {elemento} è nella lista colori")
    else:
        print(f"il colore {elemento} non è nella lista colori")

