#---------esercizio calcolatrice
# Calcolatrice semplice
while True:
    print("=== Calcolatrice ===")
    num1 = (input("Inserisci il primo numero: "))
    if not num1.isdigit():
      print("inserimento non valido")
      break
    else:
      num1 = int(num1)
    num2 = (input("Inserisci il secondo numero: "))
    if not num2.isdigit():
      print("inserimento non valido")
      break
    else:
      num2 = int(num2)
    operazione = input("Scegli l'operazione (+, -, *, /) oppure q per uscire")
    if operazione == "q":
        print("Uscita dalla calcolatrice.")
        break
    if operazione not in ['+', '-', '*', '/']:
        print("inserimento non valido")
    if operazione == "+":
        risultato = num1 + num2
    elif operazione == "-":
        risultato = num1 - num2
    elif operazione == "*":
        risultato = num1 * num2
    elif operazione == "/":
        if num2 != 0:
            risultato = num1 / num2
        else:
            risultato = "Errore: divisione per zero!"
    else:
        risultato = "Operazione non valida!"

    print(f"Risultato:, {risultato}\n")


#-------------------------usando eval
'''
def calcolatrice():
    print("=== Calcolatrice ===")
    while True:
        espressione = input("Inserisci un'espressione ('q' per uscire): ")
        if espressione.lower() == 'q':
            print("Uscita dalla calcolatrice.")
            break
        try:
            print("Risultato:", eval(espressione))
        except:
            print("Espressione non valida, riprova!")

calcolatrice()
'''

while True:
    print("=== Calcolatrice ===")
    num1 = (input("Inserisci il primo numero: "))
    if not num1.isdigit():
      print("inserimento non valido")
      break
    else:
      num1 = float(num1)
    num2 = (input("Inserisci il secondo numero: "))
    if not num2.isdigit():
      print("inserimento non valido")
      break
    else:
      num2 = float(num2)
    operazione = input("Scegli l'operazione (+, -, *, /) oppure q per uscire")
    if operazione == "q":
        print("Uscita dalla calcolatrice.")
        break
    if operazione not in ['+', '-', '*', '/']:
        print("inserimento non valido")
    if operazione == "+":
        risultato = num1 + num2
    elif operazione == "-":
        risultato = num1 - num2
    elif operazione == "*":
        risultato = num1 * num2
    elif operazione == "/":
        if num2 != 0.0:
            risultato = num1 / num2
        else:
            risultato = "Errore: divisione per zero!"
    else:
        risultato = "Operazione non valida!"

    print(f"Risultato:, {risultato}\n")