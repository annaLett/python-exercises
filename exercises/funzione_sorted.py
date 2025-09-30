#sorted riordina i caratteri
#sintassi: sorted(lista,key)
#output: lista
caratteri = ['f','d','a','c']
parole = ['ciao', 'programmazione', 'sole', 'python']

print(sorted(caratteri))
print(sorted(parole,key=len)) #con la key=len gli diciamo che deve riordinare secondo la lunghezza delle parole