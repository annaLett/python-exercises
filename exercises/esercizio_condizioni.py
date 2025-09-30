import random
#creare un generatore di numeri. 
# Una volta avviato il programma vi deve chiedere di immettere un numero nel terminale 
# e deve dirvi con un print se avete indovinato il numero o meno
'''
numero_rand = random.randint(1,10)
numero_ute = int(input("Inserisci un numero da 1 a 10 per indovinare"))

if numero_rand == numero_ute:
    print(f"Hai indovintato")
else:
    print(f"Non hai indovintato")



#con ciclo while
numero_rand = random.randint(1,10)
    
while True :
    numero_ute = input("Inserisci un numero da 1 a 10 per indovinare: ")
    if not numero_ute.isdigit(): #isdigit() controlla se il valore inserito è un numero intero, se lo è lo trasforma da string a int
        print(f"non è un numero. inserire un numero")
        continue
    if numero_rand == int(numero_ute):
        print("Hai indovinato!")
        break
    else:
        print("Non hai indovinato, riprova!")
        
'''

#gioco sasso carta forbici
#input per scegliere carta sasso forbici

numero_rand = random.randint(1,3)
scelta_utente = input("carta, sasso o forbici? ").lower()

if numero_rand == 1:
    scelta_computer = 'sasso'
elif numero_rand == 2:
    scelta_computer = 'carta'
else:
    scelta_computer = 'forbici'

print(f"il computer ha scelto: {scelta_computer}")

if scelta_utente == scelta_computer:
    print("pareggio!")
if scelta_utente == 'sasso' and scelta_computer == 'forbici': 
    print("hai vinto") 
if scelta_utente == 'forbici' and scelta_computer == 'carta': 
    print("hai vinto") 
if scelta_utente == 'carta' and scelta_computer == 'sasso': 
    print("hai vinto") 
else: 
    print("hai perso")
    
'''   


while True:
    numero_rand = random.randint(1,3)
    scelta_utente = input("carta, sasso o forbici? ").lower()

    if numero_rand == 1:
        scelta_computer = 'sasso'
    if numero_rand == 2:
        scelta_computer = 'carta'
    if numero_rand == 3:
        scelta_computer = 'forbici'

    print(f"il computer ha scelto: {scelta_computer}")

    if scelta_utente == scelta_computer:
        print("Pareggio! Gioca di nuovo.\n")
        continue

    if scelta_utente == 'sasso' and scelta_computer == 'forbici': 
        print("hai vinto") 
    if scelta_utente == 'forbici' and scelta_computer == 'carta': 
        print("hai vinto") 
    if scelta_utente == 'carta' and scelta_computer == 'sasso': 
        print("hai vinto") 
    else: 
        print("hai perso")

    break
'''