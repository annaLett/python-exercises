
#dizionario 
#vengono usati molto anche come db
#collezione non ordinata
#ogni chiave è unica e serve per accedere al valore corrispondente
# dichiariamo un dizionario usando le graffe.
# Sulla dìsinistra dichiariamo la 'chiave' e dopo il : dichiariamo il valore di quella chiave.

diz = {
    'chiave' : 'valore'
}

frutta = {
    'mela':3,
    'pera':5,
    'arancia':6
}

persona = {
    'nome': 'leonardo',
    'cognome': 'mazzoleni',
}

# Accediamo ai singoli valori del dizionario (come con le liste)
# usando le [] dopo il nome del dizionario e passando il nome della chiave tra ''
print(persona['nome'])

# I dizionari si possono ciclare, di base per ogni ciclo ritornano solo la chiave
# Per accedere al valore vale lo stesso concetto di sopra 'print(persona['nome'])'
for chiave in persona:
    print('riga:', persona[chiave])

# Se aggiungiamo il .values() dopo il nome del dizionario invece della chiave
# il for a ogni ciclo ritorna il valore invece della chiave
for valore in persona.values():
    print(valore)

# Se aggiungiamo il .items() dopo il nome del dizionario invece della chiave o del valore
# al for vengono ritornati due valori, ovvero la chiave e il valore.
for chiave, valore in persona.items():
    print(f'chiave: {chiave}, valore: {valore}')

# Aggiungere un valore al dizionario
persona['capelli'] = 'castani'
print(persona)

# Modificare un valore del dizionario
persona['nome'] = 'leo'
print(persona['nome'])

# Rimuovere una chiave dal dizionario
persona.pop('capelli')
print(persona)

del persona['nome']
print(persona)

#--------------------
#lista di dizionari  #attenzione a decommentare che ho due dizionari chiamati dict_uno
#dict_uno = {
#    'nome':'francesca',
#    'cognome' : 'rossi'
#},
#{
#    'nome':'anna',
#    'cognome' : 'lettiero'
#}
#print(dict_uno[0]['nome'])

#------------Dizionario di dizionari -file json
#Un file JSON (JavaScript Object Notation) è un formato di testo leggibile sia da persone che da computer,
#utilizzato per scambiare dati in modo efficiente tra un server e un browser web o tra diverse applicazioni. 
#È composto da coppie "chiave-valore" e liste ordinate di valori, e la sua semplicità e indipendenza dai linguaggi 
#di programmazione lo hanno reso il formato più popolare per l'interscambio di dati sul web. '''

dict_uno = {
    'persona1':{   #persona1 e persona2 sono chiavi del dict_uno
        'nome':'francesca', #nome e cognome sono chiavi di persona1
        'cognome' : 'rossi'
        },

    'persona2':{
        'nome':'anna', #nome e cognome sono chiavi di persona2
        'cognome' : 'lettiero'
        }
}

#--------------- cicli solo su dizionario persona1
#for i in dict_uno['persona1'].values():
#    print(i)
#
#lista_persona1 = dict_uno['persona1'].values()
#if 'francesca' in lista_persona1:
#    print("francesca è presente")
#else:
#    print("francesca non è presente")
    
##----------- FUNZIONE .keys()
#lista_chiavi_persona1=dict_uno['persona1'].keys()
#print(lista_chiavi_persona1)
#

#----------FUNZIONE .items() e list()
#lista_coppie_persona1 = list(dict_uno['persona1'].items()) #list() prende un oggetto iterabile e lo converte in liste
#print(lista_coppie_persona1)
#chiave1, valore1 = lista_coppie_persona1[0]
#print(f"chiave: {chiave1}, valore: {valore1}")

#------------iterazioni sugli elementi
#iterazioni sulle chiavi
for k in dict_uno.keys():
    print(f"Chiave: {k} , -> Valore : {dict_uno[k]}")
#iterazioni sugli elemeenti - items
print(dict_uno['persona1'].items())
for k,v in dict_uno['persona1'].items():
    print(f"{k},->{v}")
#iterazioni sui valori
for v in dict_uno.values():
    print(f"valore {v}")