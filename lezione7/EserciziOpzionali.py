#1. Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, 
#o None se il valore non è presente.
"""
def trova_la_chiave (dizionario, valore):
    for chiave, val in dizionario.items():
        if val == valore:
            return chiave
    return None

dizionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 2
}
valore_da_trovare = 1
chiave = trova_la_chiave(dizionario, valore_da_trovare)
print(chiave) 
"""

#2. Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.
"""
def inverti_scarta(dizionario, ):
    nuovo_dict={}
    for chiave, valore in dizionario.items():
        if valore in nuovo_dict:
            nuovo_dict[valore].append(chiave)
        else:
            nuovo_dict[valore]=[chiave]
    return nuovo_dict

dizionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 2
}
nuovo_dict=inverti_scarta(dizionario)
print(nuovo_dict)
"""

#3. Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, 
#e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.
"""
def moltiplica_numeri_pari(list_numeri, valore):
    nuova_lista=[]
    for numero in lista_numeri:
        if numero % 2 == 0:
            numero_moltiplicato = numero * 2
            nuova_lista.append(numero_moltiplicato)
    return nuova_lista

lista_numeri = (2,3,4,6,7,8,10)
valore = 2
nuova_lista=moltiplica_numeri_pari(lista_numeri, valore)
print(nuova_lista)
"""

# 4. Scrivi una funzione che determina se un numero è 'magico'. 
# Un numero è considerato magico se è divisibile per 4 ma non per 6.
"""
def determina_numero_magico(lista_numeri):
    risultati = []
    for numero in lista_numeri:
        if numero % 4 == 0 and numero % 6 != 0:
            risultati.append(f'{numero}: {True}')
        else:
            risultati.append(f'{numero}: {False}')
    return risultati

# Esempio di utilizzo
lista_numeri = [2, 3, 4, 6, 7, 8, 10]
risultati = determina_numero_magico(lista_numeri)
for risultato in risultati:
    print(risultato)
"""

#5. Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.
"""
def somma_di_numeri(lista_numeri):
    somma = 0
    for numero in lista_numeri:
        if numero % 2 == 0 or numero % 3  == 0:
            somma += numero
    return somma

lista_numeri = [2, 3, 4, 6, 7, 8, 10]
somma = somma_di_numeri(lista_numeri)
print(somma)
"""

#6. Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario 
# con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
"""
def crea_dizionario(lista_prodotti):
    lista_aggiornata={}
    for prodotto, prezzo in lista_prodotti.items():
        if prezzo > 20:
            prezzo_scontato = "{:.2f}".format(prezzo * 0.9)
            lista_aggiornata[prodotto] = prezzo_scontato
    return lista_aggiornata




lista_prodotti={'chips':20.50,
              'cola':10,
              'gelato':21}
lista_aggiornata=crea_dizionario(lista_prodotti)
print(lista_aggiornata)
"""

#7. Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
# e aggrega i voti per studente in un nuovo dizionario.