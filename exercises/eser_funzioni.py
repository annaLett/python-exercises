'''
def quante_parole():
    numero = int(input"quante parole vuoi inserire")
    return numero
def contatore ():
    contatore=[]
    return contatore
def ciclo(numero):
    contatore()
    
''' #DA FINIRE ultimo ese slide del 25/09

 #Scrivi un programma, utilizzando le funzioni,  che:
 #1.Chieda all’utente di inserire un numero intero, che indica
 #quante parole vuole inserire.
 #2.Inizializzi un contatore a 0 e una lista vuota.
 #3.Usi un ciclo while che continua finché il contatore è minore
 #del numero inserito.
 #4.Ad ogni iterazione del ciclo:
 #chieda all’utente di digitare una parola,
 #aggiunga la parola alla lista.
 #incrementi il contatore di 1.
 #Stampa la lista di parole


#controlla se il numero inserito è intero
def numero():
  while True:
    num = input(f"quante parole vuoi inserire? Per chiudere digita una lettera\n")
    if not num.isdigit():
      print("Hai inserito una lettera, sei uscito dal programma")
    else:
      num = int(num)
    return num

def popola(num_parole,conta):
 lista_parole=[]
 while conta<num_parole:
   parola=input("inserisci una parola")
   lista_parole.append(parola)   
   conta +=1 
 return lista_parole

numero_parole = numero()
lista_totale = popola(numero_parole, 0)
print(lista_totale)