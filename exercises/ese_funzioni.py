#crea due liste di frutta


def unisci(uno, due):
    lista_unita = uno + due 
    #print(f"somma: {lista_unita} ")
    return lista_unita
def duplica(uno,due):   
    duplicato=unisci(uno,due)*2
    #print(f"duplicazione: {duplicato} ")
    return duplicato
 
frutta1 = ["mela","banana"]
frutta2 = ["arancia","pera"]   
#unisci(frutta1,frutta2) solo se la funzione termina con print, con return allochiamo una variabile es. frutta_totale
#duplica(frutta1,frutta2)

frutta_totale = unisci(frutta1,frutta2)
frutta_perdue = duplica(frutta1,frutta2)
print(frutta_totale, frutta_perdue)