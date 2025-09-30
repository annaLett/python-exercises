##------1 Scrivi un programma che chieda all’utente di inserire una parola o una frase 
#--------e poi stampi la stessa stringa al contrario.

#def parola():
#    return input("inserisci una parola o una frase: ")
#def stampa_contrario():
#    return print(f"{parola()[::-1]}")
#                 
#stampa_contrario()


#------2 Scrivi un programma che prenda in input un numero n 
#--------e crei una lista di tutti i numeri pari da 0 fino a n. Stampa la lista.

#def prendi_numero():
#    while True:
#        numero = input("inserisci un numero positivo: ")
#        if not numero.isdigit():
#            print("inserimento non valido, inserire un numero")
#            continue
#        else:
#           numero = int(numero)
#           break
#    return numero
#
#def tutti_pari():
#    n=prendi_numero()
#    pari = []
#    num = 0
#    while num <= n:
#        if num % 2 == 0:
#            pari.append(num)
#        num+= 1
#    return print(f"i numeri pari fino a {n} sono {pari}")
   
#tutti_pari()





#Rubrica telefonica
#Crea un piccolo programma che permetta di gestire una rubrica telefonica.
#Funzionalità minime richieste:
#Aggiungere un contatto (nome + numero).
#Cercare un contatto per nome.
#Visualizz{are tutti i contatti.
#aggiungi opzione elimina

def aggiungi_contatto(rub):
    nome = input(f"Digita nome contatto da aggiungere: \n")
    
    while True:
        numero = input(f"Digita numero contatto da aggiungere: \n")
        if not numero.isdigit():
            print("inserimento non valido, inserire un numero di telefono di sole cifre numeriche")
            continue
        else:
           numero = int(numero)
           rub[nome] = numero
           break
    print(f"Hai aggiunto {nome} in rubrica con numero {numero} ")
    return rub
        
def cerca_contatto(rubrica):
    nome = input("Che contatto vuoi cercare? \n").lower()
    for contatto in rubrica:
        if contatto.lower() == nome:
            print(f"{contatto} è presente con numero: {rubrica[contatto]}")
            return
    print(f"{nome} non è presente")

def visualizza(rubrica):
    print("-----------Rubrica-----------")
    for k,v in rubrica.items():
        print(f"nome: {k} , numero: {v}")

def elimina_contatto(rubrica):
    nome = input("Quale contatto vuoi eliminare? \n").lower()
    for contatto in rubrica:  
        if contatto.lower() == nome:
            rubrica.pop(contatto)
            print(f"Il contatto {contatto} è stato eliminato")
            return rubrica


rubrica = {
    'Mario': 112345678,
    'Maria': 112234567,
    'Pippo': 112233456,
    'Gigi' : 123123123
}


while True:
    richiesta_ute = input("##Che azione vuoi effettuare?##\n Ricerca -> 1\n Vista -> 2\n Aggiungi contatto -> 3\n Rimuovi contatto -> 4\n Digita q per uscire\n")
    if richiesta_ute == "1":
        cerca_contatto(rubrica)
    elif richiesta_ute == "2":
        visualizza(rubrica)
    elif richiesta_ute == "3":
        aggiungi_contatto(rubrica)
    elif richiesta_ute == "4":
        elimina_contatto(rubrica)
    elif richiesta_ute == 'q':
        break
    else:
        print("Nessuna azione valida selezionata")
    continue