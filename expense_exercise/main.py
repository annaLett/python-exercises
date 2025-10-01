import expenses
'''Un utente vuole tenere traccia delle sue spese giornaliere 
(alimentari, trasporti, divertimento, ecc.) e avere strumenti per analizzarle.

Lo script deve:

1. Creare una lista vuota di spese.
2. Usare le funzioni del modulo per aggiungere spese in categorie diverse.
3. Stampare:
   - Il totale delle spese
   - Le spese in una categoria scelta (es. "alimentari")
   - La categoria più costosa
   - La media delle spese


'''

spese = []

spese = expenses.aggiungi_spesa(spese, "alimentari", 25.5)
spese = expenses.aggiungi_spesa(spese, "alimentari", 25.5)
spese = expenses.aggiungi_spesa(spese, "trasporti", 10)
spese = expenses.aggiungi_spesa(spese, "cinema", 8.5)

#print(expenses.totale_spese(spese))
#print(expenses.spese_per_categoria(spese, 'alimentari'))
#print(expenses.categoria_piu_costosa(spese))
#print(expenses.media_spese(spese))

while True:
    richiesta_ute = input("\n##Che azione vuoi effettuare?##\n Aggiungere spesa -> 1\n Totale spese -> 2\n Mostra spese per categoria -> 3\n Categoria più costosa -> 4\n Media spese totali -> 5\n Digita q per uscire\n")
    if richiesta_ute == "1":
        categoria = input("Inserisci categoria: ")
        importo = float(input("Inserisci importo: "))
        spese = expenses.aggiungi_spesa(spese, categoria, importo)
        print(f"---------------Spesa aggiunta")
    elif richiesta_ute == "2":
        print("---------------Il totale delle spese è: ",expenses.totale_spese(spese))
    elif richiesta_ute == "3":
        categoria = input("Inserisci categoria: ")
        print(f"---------------Il totale per {categoria} è {expenses.spese_per_categoria(spese, categoria)}")
    elif richiesta_ute == "4":
        print("---------------La categoria più costosa è: ",expenses.categoria_piu_costosa(spese))
    elif richiesta_ute == "5":
        print("---------------La media delle spese è: ",expenses.media_spese(spese))
    elif richiesta_ute == 'q':
        break
    else:
        print("Nessuna azione valida selezionata")
    continue