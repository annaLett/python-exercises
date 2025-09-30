#-----------Costrutto if---------------
a = int(input("scrivi un numero > 10"))

if a > 10:
    print(f"bravo")
print("hai finito") #legge "hai finito" sempre
#-----------Esercizio---------------
voto = int(input("scrivi il tuo voto (da 0 a 10)"))

if voto>5:
    print(f"è sufficiente")
print("fine") #legge "fine" sempre

#-----------Costrutto if else---------------
voto = int(input("scrivi il tuo voto (da 0 a 10)"))

if voto>5:
    print(f"è sufficiente")
else:
    print(f"è insufficiente")
print("fine") #legge "fine" sempre

#-----------es pari e dispari---------------
nume_int = int(input("inserisci un numero"))

if nume_int%2 == 0:
    print(f"Hai inserito un numero pari")
else: 
    print(f"Hai inserito un numero dispari")
    

#-----------es sconto--------------
totale_spesa = float(input("Inserire l'importo totale della spesa"))
sconto_10 = totale_spesa* 0.90
sconto_5 = totale_spesa*0.95
if totale_spesa >= 50:
    print(f"Hai ottenuto uno scontro del 10%, paghi in totale: {sconto_10}")
else:
    print(f"Hai ottenuto uno scontro del 5%, paghi in totale: {sconto_5}")
print(f"Arrivederci")


#----------Costrutto if elif else----------
temperatura = int(input("Inserire temperatura"))

if temperatura >= 25 :
    print(f"Fa' caldo")
elif temperatura >= 15 :
    print(f"Clima temperato")
else :
    print(f"Fa' freddo")
    
#---------Esercizio if elif else
totale_spesa = float(input("Inserire l'importo totale della spesa"))

if totale_spesa > 100:
    totale_spesa = (totale_spesa*0.80) - 10
    print (f"Hai ottenuto uno scontro del 20%, e ulteriori 10 euro di sconto, paghi in totale: {totale_spesa}")
elif totale_spesa >= 50 and totale_spesa <= 100 :
    totale_spesa = totale_spesa* 0.90
    print (f"Hai ottenuto uno scontro del 10%, paghi in totale: {totale_spesa}")
else:
    totale_spesa = totale_spesa+5
    print (f"Ti addebiteremo 5 euro di consegna, paghi in totale: {totale_spesa}")
    
#-------------esercizio booking
notti = int(input("quante notti resti in hotel? "))
stanza = input("che stanza vuoi? (singola/doppia/suite)").lower #funzione per ovviare al problmea delle maiuscole
costo_totale = 0
tassa_soggiorno = 2
if stanza == 'singola':
    costo_totale = costo_totale + (50*notti)
    if notti > 5:
        costo_totale = costo_totale*0.90
elif stanza == 'doppia' : 
    costo_totale = costo_totale + (90*notti)
    if notti > 3:
        costo_totale = costo_totale*0.95
else:
    costo_totale = costo_totale + (150*notti)
    if notti>2:
        costo_totale = costo_totale * 0.85

costo_totale = costo_totale - tassa_soggiorno*notti
print(f"il costo totale del soggiorno è : {costo_totale}")
        
        