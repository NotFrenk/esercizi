#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def sum_above_threshold(numbers: list[int],threshold:int) -> int:
    lista = []

    for numero in numbers:
        if numero > threshold:
            lista.append(numero)
    return sum(lista)
    

print(sum_above_threshold([15, 5, 25], 20))