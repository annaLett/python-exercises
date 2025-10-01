''''
Il modulo deve contenere le seguenti funzioni:

1. aggiungi_spesa(spese, categoria, importo)
   - Aggiunge una nuova spesa alla lista delle spese.
   - Ogni spesa è rappresentata come un dizionario, es:
     {"categoria": "alimentari", "importo": 25.5}

2. totale_spese(spese)
   - Restituisce il totale delle spese.

3. spese_per_categoria(spese, categoria)
   - Restituisce il totale delle spese per una specifica categoria.

4. categoria_piu_costosa(spese)
   - Restituisce la categoria con la spesa totale più alta.

5. media_spese(spese)
   - Restituisce la media delle spese inserite.


'''
def aggiungi_spesa(spese, categoria, importo):
    spese.append({"categoria": categoria, "importo": importo})
    return spese

def totale_spese(spese):
    return sum(spesa["importo"] for spesa in spese)
        
def spese_per_categoria(spese, categoria):
    return sum(spesa["importo"] for spesa in spese if spesa["categoria"] == categoria)

def categoria_piu_costosa(spese):
    # Creiamo un dizionario che somma le spese per categoria
    totali = {}
    for spesa in spese:
        cat = spesa["categoria"]
        totali[cat] = totali.get(cat, 0) + spesa["importo"]
    
    # Troviamo la categoria con il totale più alto
    if not totali:
        return None  # caso lista vuota
    return max(totali, key=totali.get)

def media_spese(spese):
    if not spese:  # lista vuota
        return 0
    return totale_spese(spese) / len(spese)