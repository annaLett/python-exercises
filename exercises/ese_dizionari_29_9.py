##dict_uno = {
#    'persona1':{   #persona1 e persona2 sono chiavi del dict_uno
#        'nome':'francesca', #nome e cognome sono chiavi di persona1
#        'cognome' : 'rossi'
#        },
#
#    'persona2':{
#        'nome':'anna', #nome e cognome sono chiavi di persona2
#        'cognome' : 'lettiero'
#        }
#}
#
##---------------
#for i in dict_uno['persona1'].values():
#    print(i)

#----------ese
    
def stampa_voti(voti):
    print("I voti sono: ", list(voti.values()))
        
def stampa_nomi_voti(voti):
    for k,v in voti.items():
        print(f"{k} ha voto: {v}")
        
def media_voti(voti):
    media=sum(voti.values())/(len(voti))
    print(f"La media dei voti è: {round(media)}")
    
def voto_massimo(voti):
    voto_massimo=0
    for v in voti.values():
        if v > voto_massimo:
            voto_massimo = v
    print(f"Il voto più alto è: {voto_massimo}")
  
def aggiungi(voti, nome,voto):
    voti[nome] = voto
    print(voti)  

voti = {
    'Anna':28,
    'Luca':22,
    'Marco':30,
    'Sara':18,
    'Giulia':25
}

stampa_voti(voti)
stampa_nomi_voti(voti)
media_voti(voti)
voto_massimo(voti)
aggiungi(voti, 'Carlo', 20)  