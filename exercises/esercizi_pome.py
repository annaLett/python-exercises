#Stampa i primi 3 elementi della lista frutta.
frutta = ['mela','pera','banana','pomodoro','anguria']
print(*frutta[0:3])

#Stampa tutti gli elementi tranne il primo e l’ultimo.
print(*frutta[1:-1])

#Usa un ciclo for per stampare ogni frutto della lista frutta in maiuscolo.
for frutto in frutta:
    print(frutto.upper())
    
#Chiedi all’utente di inserire un frutto.
while True:
    frutto_new = input("inserire un frutto nuovo ")
    if frutto_new in frutta:
        continue
    else:
        frutta.append(frutto_new)
    break

#Controlla se il frutto è presente nella lista frutta e stampa un messaggio appropriato.
print(f"è stato correttamente aggiunto il frutto: {frutto_new}, nuova lista", *frutta)

