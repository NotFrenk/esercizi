#Scrivi una funzione che accetti tre parametri: 
#username, password e status di attivazione dell'account (attivo/non attivo). 
#L'accesso è consentito solo se il nome utente è "admin", 
#la password corrisponde a "12345" e l'account è attivo. 
#La funzione ritorna "Accesso consentito" oppure "Accesso negato".
"""
def check_access(username:str,password:str,status:bool):
    if username == "admin" and password == 12345 and status == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
risultato=check_access("admin", 12345, "attivo")
print(risultato)
"""

#Scrivi una funzione che calcola la media di una lista di numeri 
#e ritorna il valore arrotondato all'intero più vicino.
"""
def rounded_average(numbers: list[int]) -> int:

    media=sum(numbers) / len(numbers)
    media_arrotondata=round(media)
    return media_arrotondata

print(rounded_average([1, 1, 2, 2]))
"""


#Scrivi una funzione che somma tutti i numeri interi 
#di una lista che sono maggiori di un dato valore intero definito threshold.
"""
def sum_above_threshold(numbers: list[int], threshold:int) -> int:
    r:int=0
    for x in numbers:
        if x > threshold:
            r=r+x
    return r
print(sum_above_threshold([15, 5, 25], 20))
"""

#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) 
#è soddisfatta per procedere con un'operazione. 
#L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
#La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" 
#a seconda delle condizioni che sono soddisfatte.
"""
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA==True:
        return "Operazione permessa"
    elif conditionB==True and conditionC ==True:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
print(check_combination(True, False, True))
print(check_combination(False, True, False))
"""

#Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". 
#Un numero magico è definito come un numero che contiene il numero 7.
"""
def is_magic_number(num: int) -> bool:
    numero_stringa=str(num)
    if "7" in numero_stringa:
        return True
    else:
        return False
print(is_magic_number(70))
"""

#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, 
#mantenendo l'ordine originale degli elementi.
"""
def remove_duplicates(lista:list[int,str]) -> list:
    elementi_unici:list=[]
    for x in lista:
        if x not in elementi_unici:
            elementi_unici.append(x)
    return elementi_unici

lista = [1, 2, 3, 2, 'a', 'b', 'a', 3]
print(remove_duplicates)

"""

#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate,
#cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
"""
def check_parentheses(expression: str) -> bool:
    ogni_elemento=[]
    for x in expression:
        if x== "(":
            ogni_elemento.append(x)
        elif x==")":
            if not ogni_elemento or ogni_elemento[-1] != '(':
                return False
            ogni_elemento.pop()
    return len(ogni_elemento) == 0


print(check_parentheses("()()"))
"""

#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
#Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
"""
def count_isolated(lista_numeri:list[int]) -> int:
    numeri_isolati:list[int]=0
    for numero in range(len(lista_numeri)):
        if numero==0 and lista_numeri[numero] !=lista_numeri[numero+1]:
            numeri_isolati += 1
        elif numero==len(lista_numeri) -1 and lista_numeri[numero] != lista_numeri[numero-1]:
            isolati += 1
        elif lista[i] != lista[i - 1] and lista[i] != lista[i + 1]:
            isolati += 1
    
    return isolati
"""


#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
#ritorni un nuovo insieme senza i numeri specificati nella lista.
"""
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    return original_set - set(elements_to_remove)
print(remove_elements({5, 6, 7}, [7, 8, 9]))
"""

#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
"""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    risultato = {}
    
    for chiave in dict1:
        if chiave in dict2:
            risultato[chiave] = dict1[chiave] + dict2[chiave]
        else:
            risultato[chiave] = dict1[chiave]
    
    for chiave in dict2:
        if chiave not in dict1:
            risultato[chiave] = dict2[chiave]
    
    return risultato

"""

