#split()
#trasforma una stringa in una lista

stringa = "ciao come stai"
lista_stringa = stringa.split()
print(lista_stringa)
print(*lista_stringa) #asterisco per visualizzare meglio

#es data la stringa convertirla in una lista di frutti
frutti = "mela,banana,pera"
lista_frutti = frutti.split(',') #metto la virgola che è il valore che mi definisce gli elementi della lista
print(frutti)
print(*lista_frutti) 