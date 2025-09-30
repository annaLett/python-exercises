import random
'''# generare una password alfanumerica randomica
# fare il print della password a schermo

import random
# generare una password alfanumerica randomica
# fare il print della password a schermo

password = ''

lettere = 'abcdefghilmno'
numeri = '1234567890'
caratteri_speciali = '#@[]$!?=&/£'

while True:
    lunghezza_password = input('lunghezza password:\n')

    if not lunghezza_password.isdigit() or lunghezza_password == '0':
        print('Inserisci un numero valido!')
        continue

    break

for _ in range(int(lunghezza_password)):
    random_number = random.randint(1, 3)

    # genera un lettera
    if random_number == 1:
       letters_random_number = random.randint(0, len(lettere) - 1)
       password = password + lettere[letters_random_number]

    # genera un numero
    elif random_number == 2:
       numbers_random_number = random.randint(0, len(numeri) - 1)
       password = password + numeri[numbers_random_number]

    # genera un caratere speciale
    else:
        special_random_number = random.randint(0, len(caratteri_speciali) - 1)
        password = password + caratteri_speciali[special_random_number]

# Assegna il maiuscolo a qualche lettera
for carattere in password:
    if carattere.isalpha():
        random_number_upper = random.randint(1, 100)
        if random_number_upper > 70:
            password = password.replace(carattere, carattere.upper())



print('La tua password è: ', password)
'''
#-------------------Scrivere un programma Python che generi password randomica
# - contenente lettere (maiuscole e minuscole), numeri e caratteri specilai
# - Chiedere all'utente la lunghezza della password.
# - Fare il print della password alla fine del programma.
'''
lunghezza_password = int(input("inserire lunghezza password: "))
lettere = 'abcdefghilmno'
numeri = '1234567890'
caratteri_speciali = '#@[]$!?=&/£'
password = []
while len(password)<lunghezza_password:
    password.append(lettere[random.randint(0, len(lettere)-1)])
    password.append(numeri[random.randint(0, len(numeri)-1)])
    password.append(caratteri_speciali[random.randint(0, len(caratteri_speciali)-1)])

for i in range(len(password)):
    if password[i].isalpha():
        if random.randint(1, 100) <= 30:
            password[i] = password[i].upper()
        
print(password)


lunghezza_password = int(input("inserire lunghezza password: "))
lettere = 'abcdefghilmno'
numeri = '1234567890'
caratteri_speciali = '#@[]$!?=&/£'


def crea(lunghezza_psw, lettere, numeri, caratteri_speciali):
    password = []
    while len(password)<lunghezza_psw:
    password.append(lettere[random.randint(0, len(lettere)-1)])
    password.append(numeri[random.randint(0, len(numeri)-1)])
    password.append(caratteri_speciali[random.randint(0, len(caratteri_speciali)-1)])
    
    return password

password = crea(lunghezza_password,lettere,numeri,caratteri_speciali)

#correzione Leonardo
import random

lunghezza_password = int(input("inserire lunghezza password: "))
lettere = 'abcdefghilmno'
numeri = '1234567890'
caratteri_speciali = '#@[]$!?=&/£'
password = []
while len(password)<lunghezza_password:
    password.append(lettere[random.randint(0, len(lettere)-1)])
    password.append(numeri[random.randint(0, len(numeri)-1)])
    password.append(caratteri_speciali[random.randint(0, len(caratteri_speciali)-1)])

#in generale meglio usare un while loop invece di un for
i = 0
while i < len(password):
    if password[i].isalpha():
        if random.randint(1, 100) <= 30: #qui mi calcola la probabilità su ogni singola lettera e non sul totale della password 
            password[i] = password[i].upper()
    i +=1
        
print("".join(password)) #questo join ci permette di unire i valori di una stringa e tra virgolette ci possiamo mettere i valori che vogliamo es.","
'''
import random

lunghezza_password = int(input("inserire lunghezza password: "))
lettere = 'abcdefghilmno'
numeri = '1234567890'
caratteri_speciali = '#@[]$!?=&/£'
tutto = lettere+numeri+caratteri_speciali
password = []
while len(password)<lunghezza_password:
    password.append(lettere[random.randint(0, len(lettere)-1)])
    password.append(numeri[random.randint(0, len(numeri)-1)])
    password.append(caratteri_speciali[random.randint(0, len(caratteri_speciali)-1)])

#in generale meglio usare un while loop invece di un for
i = 0
while i < len(password):
    if password[i].isalpha():
        if random.randint(1, 100) <= 30: #qui mi calcola la probabilità su ogni singola lettera e non sul totale della password 
            password[i] = password[i].upper()
    i +=1
        
print("".join(password)) #questo join ci permette di unire i valori di una stringa e tra virgolette ci possiamo mettere i valori che vogliamo es.","