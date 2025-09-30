
mesi_abbonamento = int(input("abbonamento per quanti mesi?"))
tipo_abbonamento = input("quanle tipo di abbonamento? (base/premium/vip)").lower()
iscrizione = 0 #tassa di iscrizione già presente
if tipo_abbonamento == 'base':
    iscrizione = 30*mesi_abbonamento
    if mesi_abbonamento > 6:
        iscrizione = iscrizione*0.95
elif tipo_abbonamento == 'premium' : 
    iscrizione = 50*mesi_abbonamento
    if mesi_abbonamento > 2:
        iscrizione = iscrizione*0.90
else:
    iscrizione = 80*mesi_abbonamento
    if mesi_abbonamento>12:
        iscrizione = iscrizione * 0.80
        
iscrizione = iscrizione + 20
print(f"l'abbonamento costa : {iscrizione}")

'''


while True:
    
    iscrizione = 0 
    mesi_abbonamento = input("abbonamento per quanti mesi?")
    
    if not mesi_abbonamento.isdigit():
        print(f"non è stato inserito un numero. inserire un numero di mesi")
        continue
    
    tipo_abbonamento = input("quanle tipo di abbonamento? (base/premium/vip)").lower()
    iscrizione = 20 #tassa di iscrizione già presente
    
    if tipo_abbonamento == 'base':
        iscrizione = iscrizione + (30*mesi_abbonamento)
        if mesi_abbonamento > 6:
            iscrizione = iscrizione*0.95
    if tipo_abbonamento == 'premium' : 
        iscrizione = iscrizione + (50*mesi_abbonamento)
        if mesi_abbonamento > 2:
            iscrizione = iscrizione*0.90
    else:
        iscrizione = iscrizione + (80*mesi_abbonamento)
        if mesi_abbonamento>12:
            iscrizione = iscrizione * 0.80
    break            
print(f"l'abbonamento costa : {iscrizione +20}")
    
'''