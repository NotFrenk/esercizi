#Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dizionario = {
        'pari':[],
        'dispari':[]
    }
   
    for numero in lista:
        if numero % 2 == 0:
            dizionario['pari'].append(numero)
        else:
            dizionario['dispari'].append(numero)
    return dizionario


print(classifica_numeri([1, 2, 3, 4, 5, 6]))