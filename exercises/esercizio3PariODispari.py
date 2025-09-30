import random
#voglio un programma che controlli se un numero
#è pari o dispari
#se è pari stampo "è pari"
#se è dispari stampo "è dispari"

numero = random.randint(1,100)

if numero % 2 == 0:
    print(f"il numero {numero} è pari")
else:
    print(f"il numero {numero} è dispari")