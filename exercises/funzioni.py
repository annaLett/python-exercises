#esercizio riscaldamento con while
lista_num = []
while True:
    numero = input(f"Inserisci un numero")
    if not numero.lstrip('-').isdigit(): #lstrip conta come eccezione il segno meno, per inserire numeri negativi
        break
    else:
        lista_num.append(int(numero))
        
print(f"hai inserito: {lista_num}")

#oggi Liste - Stringhe - Funzioni
#una stringa è una lista di caratteri
#operatori di confronto: == , < , <= ,>,>= , !=

lista_uno = [2,4,8]
lista_due = [5,6,7]

#confrontro singoli numeri della lista con indice
if lista_uno[0]>lista_due[0]:
    print("il primo numero della lista uno è maggiore")
else:
    print("il primo numero della lista uno è minore")

#confronto uguaglianza lista
if lista_uno == lista_due:
    print("le liste sono uguali")
else:
    print("le liste sono diverse")
    
#confronto maggiore
if lista_uno > lista_due:
    print("la lista 1  maggiore")
else:
    print("a lista 2 maggiore")

#esercizio
numeri = [10,20,30]
if numeri[0]>numeri[-1]:
    print("il primo numero della lista è maggiore")
else:
    print("il primo numero della lista è minore")
    

testo = "Francesca"
print(testo[0]) #stampo la prima lettera, non posso manipolarle però tipo sostituire o metterle minuscole
print(len(testo)) #conto quanti caratteri ha, se metto lo spazio conta lo spazio

print(testo[-2::]) #voglio ultimi due caratteri con slicing
if 'r' in testo:   #posso controllare se un carattere è nella lista
    print('appartiene')
    
print(testo[::-1])

if testo[0] < testo[-1]:
    print(f"la lettera {testo[0]} viene prima della lettera {testo[-1]}")
else:
    print(f"la lettera {testo[-1]} viene prima della lettera {testo[0]}")

  
parola = "Università"  
#primo e ultimo carattere
print(parola[0::9])
#lunghezza stringa
print(len(parola))
#stampa dal secondo al quarto usando lo slicing
print(parola[1:4])
#controlla se il carattere "i" è presente nela stringa
if 'i' in parola:
    print('i è presente')
else:
     print('i non è presente')

#conta quante i ci sono
conto = 0
for carattere in parola:
    if carattere == 'i':
        conto += 1
print(f'i è presente {conto} volte')
     

#------------FUNZIONI

def saluta():
    nome=input("come ti chiami?")
    print(f"ciao {nome}")
    
def mostra_programma():
    saluta()
#richiamo per far partire, partirebbe anche solo con saluta(), mostra è per far vedere che si possono richiamare in un altra funzione
mostra_programma()

def saluta_nome(nome):
    print(f"ciao {nome} benvenuto")
    
nome = 'anna'
saluta_nome(nome)
#-----------
def saluta(nome, cognome):
    print(f"ciao {nome} {cognome}")
#nome = input("inserisci nome: ")
#cognome = input("inserisci cognome: ")

#saluta(nome,cognome)
saluta('mario','rossi')
saluta(1,2)