# 1. 
# Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, 
# o None se il valore non è presente.
"""
def prendi_valore (dizionario:dict, valore:int):
    for chiave, valore_dict in dizionario.items():
        if valore_dict == valore:
            return chiave
        else:
            return None
        
dizionario1= {
    'Mela':1,
    'Pera':2,
    'Macchina':3
}

print(prendi_valore(dizionario1, 1))
print(prendi_valore(dizionario1, 5))
"""

# 2. 
# Scrivi una funzione che inverte le chiavi e i valori in un dizionario. 
# Se ci sono valori duplicati, scarta i duplicati.
"""
def inverti_oggetti(dizionario:dict):
    
    dizionario_invertito = {}

    valori_visti = set()

    for chiave, valore_chiave in dizionario.items():
        if valore_chiave not in valori_visti:
            dizionario_invertito[valore_chiave]=chiave
            valori_visti.add(valore_chiave)
    
    return dizionario_invertito

dizionario1 = {
    'Casa':1,
    'Macchina':2,
    'Balcone':3,
    'Farmacia':2
}

dizionario_invertito = inverti_oggetti(dizionario1)
print(dizionario_invertito)
"""

# 3. 
# Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, 
# e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.
"""
def filtra_lista(lista:list, fattore:int):

    new_list:list = []

    for numero in lista:
        if numero % 2 == 0:
            numero *= fattore
            new_list.append(numero)
    print(f'{new_list}')


numeri = [1,2,3,4,5,6,7,8,9,10]
fattore = 3
numeri_filtrati = filtra_lista(numeri, fattore)
"""

# 4. 
# Scrivi una funzione che determina se un numero è 'magico'. 
# Un numero è considerato magico se è divisibile per 4 ma non per 6.
"""
def determina_Se(lista:list):

    new_list=[]

    for numero in lista:
        if numero % 4 == 0 and numero % 6 != 0:
            new_list.append(numero)

    return new_list if new_list else None
    
numeri = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(determina_Se(numeri))
"""

#5. 
# Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.
"""
def somma_numeri(lista:list):

    lista2 = []

    for numero in lista:
        if numero %2 == 0 and numero %3 == 0:
            lista2.append(numero)
    
    return sum(lista2)

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(somma_numeri(numeri))
"""

