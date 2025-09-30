#-----ciclo a priori - CICLO WHILE
conta = 0
lista = []
while conta<5:
    num = int(input("inserisci un numero: "))
    conta = conta + 1
    lista.append(num)
    print(f"il {conta}° numero inserito è {num}")
print(lista)

#esercizio
quantita = int(input(f"Quante parole vuoi inserire?"))
conta = 0
while conta <quantita:
    parola = input(f"Digita una parola ")
    conta = conta + 1
    print(f"la {conta}° parola inserita è {parola}")
 
 
 #-----------Controllo input utente-------------
while not(testo_digitato.isdigit()):
    print("ERRORE scrivi un numero")
    testo_digitato = input("Quante parole vuoi inserire? ")
    #poi devo riconvertire testo_digitato in int

#ciclo a posteriori - CICLO DO WHILE ma in python non esiste
#quindi facciamo while True e poi usciamo con break
while True:
    num = int(input("Inserisci un numero positivo"))
    if num > 0 :
        break
print(f"Il numero positivo è: {num}")


while True:
    num = input("Inserisci un numero ")
    if not(num.isdigit()) :
        print(f"hai inserito una lettera, programma terminato")
        break
    else:
       
        print(f"Il numero è: {num}")
    