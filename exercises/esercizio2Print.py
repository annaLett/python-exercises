#stampare la somma, sottrazione, 
#moltiplicazione, divisione tra due numeri
#usare le variabili

numero1 = 4 
numero2 = 10
somma = numero1 + numero2
sottrazione = numero2 - numero1
moltiplicazione = numero1 * numero2
divisione = numero2 / numero1

print('somma',somma)
print('sottrazione',sottrazione)
print('moltiplicazione',moltiplicazione)
print('divisione',divisione)

#alternativa con f string
print (f"somma: {numero1} + {numero2} = {somma}")
print (f"sottrazione: {numero2} - {numero1} = {sottrazione}")
print (f"moltiplicazione: {numero1} * {numero2} = {moltiplicazione}")
print (f"divisione: {numero2} / {numero1} = {divisione}")

#--------------Esercizio-------------
lato = float(input("inserisci lato quadrato"))
perimetro = lato*4
print(f"il perimetro è: {perimetro}")