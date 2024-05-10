#Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, 
#e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.

"""
def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    numeri_pari = []
    numeri_pari_moltiplicati = []
    for numero in lista_numeri:
        if numero % 2 == 0:
            numeri_pari.append(numero)
        
    for numero_paro in numeri_pari:
        numeri_pari_moltiplicati.append(numero_paro*fattore)

    return numeri_pari_moltiplicati


    
print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3)) 
"""


#Scrivi una funzione che accetti una lista di numeri 
#e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.

"""
def somma_condizionale(numeri: list[int]) -> int :
    somma = 0
    for numero in numeri:
        if numero % 2 == 0 and numero % 3 == 0:
            somma += numero

    return somma

print(somma_condizionale([1, 2, 3, 6, 12]))

"""



#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
#Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
"""
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    for chiavi, numero_di_volte in da_rimuovere.items():
        for _ in range(numero_di_volte):
            if chiavi in lista:
                lista.remove(chiavi)

    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
"""


#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
#e aggrega i voti per studente in un nuovo dizionario.
"""
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    nuovo_dizionario = {}
    for studente in voti:
        nome = studente["nome"]
        voto = studente["voto"]
        
        if nome in nuovo_dizionario:
            nuovo_dizionario[nome].append(voto)
        else:
            nuovo_dizionario[nome] = [voto]

    return nuovo_dizionario


print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

"""


#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi 
# e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
"""
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    prodotti_con_sconto = {}
    for prodotto, valore in prodotti.items():
        if valore > 20:
            prezzo_scontato=valore*0.9
            prodotti_con_sconto[prodotto] = prezzo_scontato
    return prodotti_con_sconto


print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
"""


#PARTE 1
#Scrivi una funzione chiamata create_contact() 
#che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
#La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
#PARTE 2
#Scrivi una funzione chiamata update_contact() 
#che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. 
#Questa funzione dovrebbe aggiornare il dizionario del contatto.

"""

"""

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    dettagli_del_contatto = {}
    

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    pass



contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))