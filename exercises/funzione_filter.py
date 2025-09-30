#filter(condizione,lista)
#filtra gli elementi di una lista in vase a una condizione
#per condizione di intende duna funzione che prende come input
#l'elemento e ritorna True o False

#usando filter(), estrarre solo le parole più lunghe di 4 lettere dalla lista
def parole_lunghe(parola):
    return len(parola)>4

def parole_con_p(parola): #ritorna le parole che contengono la p
    return 'p' in parola

parole = ['ciao', 'programmazione', 'sole', 'python']
parola_filtrata = list(filter(parole_lunghe,parole)) #filter scorre la lista e mette le parole nella funzione sopra per poi restituire le parole che soddisfano la condizione
print(parola_filtrata)

print(list(filter(parole_con_p,parole)))

