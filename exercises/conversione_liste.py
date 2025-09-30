#------conversione da lista a stringa
#utilizziamo join()
parole = ['ciao', 'io', 'sono', 'anna']
frase = " ".join(parole) #uso lo spazio come separatore e unisco la lista sopra. potrei usare qualsiasi carattere
print(frase)
frase_a_capo = "\n".join(parole)
print(frase_a_capo)

#esercizio
#data la lista, convertirla in stringa e usa come separatore il carattere'-'

lista = [1,2,3]
lista_str = list(map(str,lista))#per convertire una lista di numeri in una lista di stringhe, si usa map e str in questo modo
print("-".join(lista_str))
