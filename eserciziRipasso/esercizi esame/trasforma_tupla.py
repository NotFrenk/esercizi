# Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
# Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:

    dizionario = {}

    for tuple in tuples:
        kay, valu = tuple
        if kay in dizionario:
            dizionario[kay].append(valu)
        else:
            dizionario[kay] = [valu]
    return dizionario

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))