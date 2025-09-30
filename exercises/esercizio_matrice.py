matrice =[
    ['x','o','x'],
    ['o','x','o'],
    ['x','x','o']
]
#-----svolgimento senza funzione
#conto_x = 0
#conto_o = 0
#for riga in matrice:
#    for elemento in riga:
#        if elemento == 'x':
#             conto_x += 1
#        else:
#            conto_o += 1
#            
#print(conto_x)
#print(conto_o)

def contax(matrice):
    conto_x = 0
    for riga in matrice:
        for elemento in riga:
            if elemento == 'x':
                conto_x += 1
    return conto_x

def contao(matrice):
    conto_o = 0
    for riga in matrice:
        for elemento in riga:
            if elemento == '0':
                conto_o += 1
    return conto_o


conto=(f"nella matrice abbiamo {contax(matrice)} x e {contao(matrice)}")
print(conto)