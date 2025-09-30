##################da aggiustare 

def mesi():
    mesi_abbonamento = input("abbonamento per quanti mesi?\n")
    if not mesi_abbonamento.isdigit():
      print("inserimento non valido")
      return None  #
    else:
      mesi_abbonamento = int(mesi_abbonamento)
    return mesi_abbonamento
    
def tipo():
    tipo_abbonamento = input("vuoi un abbonamento base, premium o vip? \n").lower()
    if tipo_abbonamento not in ['base', 'premium', 'vip']:
        print("inserimento non valido")
        return None
    else:
        tipo_abbonamento = tipo_abbonamento
    return tipo_abbonamento

def prezzo(mesi_abbonamento, tipo_abbonamento):
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
    return (iscrizione+20) #per la quota fissa di iscrizione


mesi = mesi()
tipo = tipo()
prezzo = prezzo(mesi, tipo)
print(mesi)
print(tipo)
print(f"l'abbonamento costa : {prezzo} ")