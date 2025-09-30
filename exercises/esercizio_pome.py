import random
from random import randint
'''
Genera una serie di liste in modo casuale.

Ogni lista deve contenere un numero casuale di elementi numerici.
inizzializzo due variabili random per liste ed elementi
Individua la lista centrale (quella che si trova a metà della serie).

Prima di procedere, verifica che la lista centrale contenga un numero dispari di elementi.

Se la condizione è soddisfatta, stampa il valore centrale di quella lista.



#esercizio mio
numero_liste = random.randrange(1, 10, 2) #mi generea solo dispari
numero_elementi = random.randrange(1, 10, 2)
matrice = []
i=0
while i < numero_liste:
    j = 0
    n = []
    while j < numero_elementi:
        number = randint(1,100)
        n.insert(i,number)
        j = j+1
    matrice.append(n)
    i = i+1
print(matrice)
lunghezza=len(matrice)
lista_centrale = lunghezza//2
valore_centrale_centrale=
print(lunghezza)
print(matrice[lista_centrale])
if len(matrice[lista_centrale]) /2 == 0:
    print(f"i numeri della matrice sono pari")
else:
    print(f"i numeri della matrice sono dispari")
    print(f"valore centrale: {matrice[lista_centrale][2]}")
    '''
#esercizio corretto da leonardo

numero_liste = random.randrange(1, 10, 2) #mi generea solo dispari
numero_elementi = random.randrange(1, 10, 2)
matrice = []

for numero in range(numero_liste):
    nuova_riga = []
    for elemento in range(numero_elementi):
        numero_casuale = random.randint(1, 100)
        nuova_riga.append(numero_casuale)
    matrice.append(nuova_riga)

print(matrice)
lunghezza=len(matrice)
indice_lista_centrale = lunghezza//2
lista_centrale = matrice[indice_lista_centrale]

print('lunghezza:', lunghezza)
print('lista centrale:', lista_centrale)

if len(lista_centrale) % 2 == 0:
    print(f"i numeri della matrice sono pari")
else:
    indice_numero_centrale = len(lista_centrale) // 2
    numero_centrale = lista_centrale[indice_numero_centrale]
    print('numero centrale', numero_centrale)