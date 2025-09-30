
somma = 0
Somma = 0 + 1 #python è case sensitive quindi somma e Somma non sono uguali e non stiamo aggiungendo +1
print(somma) #questo darà 0 
print(Somma) #questo darà 1 

#-------------Assegnazione Composta --------------
a = 0
a +=1 # è come fare a= a + 1
a -=1 #per decrementare una variabile
print(a)

#-------------Tipi di dati---------------------
b = 5 #int, intero
c = 4.5 #float , reale
d = 'Ciao' #stringa, testo
e = True #booleano, Ture o False
print (b,c,d,e)

#----------Casting-------------
#usiamo i metodi e la variabile tra parentesi
# float(variabile)  da un intero/stringa ad un decimale
# int(variabile)  da decimale/stringa a intero
# str(variabile)  da intero/stringa

#--------------Esercizio-------------
anno = 2025
data = "22 settembre"
da_stampare = data + (" ") + str(anno)
print(data, anno) #senza conversione
print(da_stampare)#con le conversioni

#--------------Esercizio-------------
km = 100
messaggio = "km percorsi"
stampa1 = str(km) +(" ")+ messaggio
print(f"{stampa1}")

#--------------Esercizio-------------
num1 = 10.5
num2 = "3"
divisione = 10.5/ float(num2)
print(divisione) #il risultato è un float

#--------------Istruzione Print-------
nome = "Anna"
eta = 25
print("Ciao sono " + nome + " ed ho " + str(eta) + " anni... magari") #print con + e coversione
print(f"Ciao sono {nome} ed ho {eta} anni") #print con fstring

#--------------Istruzione input()-------------
#input consente allutente di inserire un dato
nomeIn = input("come ti chiami?")
etaIn = input("quanti anni hai?")
print(nomeIn, int(etaIn)) #int()lo posso mettere qui o fuori input() es. int(input("quanti anni hai?"))

#--------------Esercizio-------------
lato = float(input("inserisci lato quadrato"))
perimetro = lato*4
print(f"il perimetro è: {perimetro}")

#-------------Esercizio---------------
base = int(input("inserisci base triangolo"))
altezza = int(input("inserisci altezza triangolo"))
area = float(base*altezza)/2
print(f"l'area è : {area}")

#-------------Esercizio---------------
prodotto_uno = float(input("inserire il prezzo del primo prodotto"))
prodotto_due = float(input("inserire il prezzo del secondo prodotto"))
prodotto_tre = float(input("inserire il prezzo del terzo prodotto"))
totale_spesa = prodotto_uno + prodotto_due + prodotto_tre
print(f"Hai comprato 3 prodotti per un totale di {totale_spesa} euro")