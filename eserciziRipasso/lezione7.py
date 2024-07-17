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