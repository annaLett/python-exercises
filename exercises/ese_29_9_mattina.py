#import utili
import random

#funzioni
def crea_matrice(num_righe, num_colonne):
    matrice = []
    for riga in range(num_righe):
        nuova_riga = []
        for elemento in range(num_colonne):
            numero_casuale = random.randint(1, 100)
            nuova_riga.append(numero_casuale)
        matrice.append(nuova_riga)
    return matrice
    
def stampa_matrice(num_righe, num_colonne):
    print(crea_matrice(num_righe, num_colonne))
    somma_righe(crea_matrice(num_righe, num_colonne))

def somma_righe(matrice):
    somma_list = []
    
    for riga in matrice:
        somma=0
        for num in riga:
            somma = somma + num
        somma_list.append(somma)
        print(f"Riga:{riga}: somma = {somma}")
   
#inizio programma
num_righe = int(input(f"quante righe?"))
num_colonne = int(input(f"quante colonne?"))
stampa_matrice(num_righe, num_colonne)

'''

#chiedo all'utente quante righe e quante colonne
num_righe = int(input(f"quante righe?"))
num_colonne = int(input(f"quante colonne?"))
matric = []
for riga in range(num_righe):
    nuova_riga = []
    for elemento in range(num_colonne):
        numero_casuale = random.randint(1, 100)
        nuova_riga.append(numero_casuale)
    matric.append(nuova_riga)
    
print(matric)

'''