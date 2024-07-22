#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for kay, valu in dict2.items():
        if kay in dict1:
            dict1[kay] += valu
        else:
            dict1[kay] = valu
    return dict1

print(merge_dictionaries({'x': 5}, {'x': -5}))