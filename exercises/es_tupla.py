def crea_tupla():
    x=int(input(f"indica x: "))
    y=int(input(f"indica y: "))
    coordinate = (x,y)
    return coordinate

def quadrante():
    x,y= crea_tupla()
    if x > 0 and y > 0:
        print(f"Il punto {x,y} si trova nel I quadrante")
    elif x < 0 and y > 0:
        print(f"Il punto {x,y} si trova nel II quadrante")
    elif x < 0 and y < 0:
        print(f"Il punto {x,y} si trova nel III quadrante.")
    elif x > 0 and y < 0:
        print(f"Il punto {x,y} si trova nel IV quadrante.")
    elif x == 0:
        print(f"Il punto {x,y} si trova sull'asse y.")
    elif y == 0:
        print(f"Il punto {x,y} si trova sull'asse x.")
    else:
        print(f"Il punto {x,y} si trova nell'origine.")
    return print 

print(quadrante())



#--------esercizio tuple mantenendo le tuple perché sopra lavoriamo con variabili
def tupla():
    x = int(input("Inserisci x: "))
    y = int(input("Inserisci y: "))
    coordinate = (x, y)
    return coordinate

def controllo_quad(tupla):
    if tupla[0]> 0 and tupla[1] > 0:
        print(f"{tupla[0]}, {tupla[1] } è nel primo quadrante")
    elif tupla[0] < 0 and tupla[1]  > 0:
        print(f"{tupla[0]}, {tupla[1] } è nel secondo quadrante")
    elif tupla[0]<  0  and tupla[1]  < 0:
        print(f"{tupla[0]}, {tupla[1] } è nel terzo quadrante")
    elif tupla[0] > 0 and tupla[1]  < 0:
        print(f"{tupla[0]}, {tupla[1] } è nel quarto quadrante")
    elif tupla[0] == 0   and tupla[1] == 0:
        print(f"{tupla[0]}, {tupla[1] } è nell'origine")


controllo_quad(tupla())

#--------------------
def potenza(n):
    quadrato = n**2
    cubo = n**3
    return quadrato, cubo #--> restituisce una tupla

#inizio
n_int = int(input("inserisci un numero intero"))
print(f"il quadrato e il cubo sono rispettivamente:{potenza(n_int)}")
quadrato, cubo = potenza(n_int) #spacchetto la tupla e assegno a due variabili
print(f"il quadrato di {n_int} è {quadrato} e il cubo di {n_int} è {cubo}")
