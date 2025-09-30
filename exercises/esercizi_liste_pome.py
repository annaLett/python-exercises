#lista con 5 frutti
#1 stampa ogni singolo elemento della lista

print(f"1 Stampa di tutti gli elementi nella lista")

frutta = ['mela','pera','banana','pomodoro','anguria']
for elemento in frutta:
    print(elemento)
#opppure print(*frutta)
#2 Stampa il primo e l’ultimo frutto della lista
print(f"2 Stampa il primo e l’ultimo frutto della lista")
print(frutta[0])
print(frutta[-1])

#3 Aggiungi un nuovo frutto alla lista frutta usando append().
frutto = input("3 scrivi un  frutto ")
frutta.append(frutto)
print("Vista lista aggiornata")
for elemento in frutta:
    print(elemento)

#4 rimuovi il secondo frutto con remove
primofrutto = frutta[1]
frutta.remove(primofrutto)
print(f"4 Lista di tutti i frutti meno il secondo")
for elemento in frutta:
    print(elemento)

#5 Usa len() per stampare quanti elementi ci sono nella lista frutta.
print("5 Lunghezza lista : ",len(frutta))
