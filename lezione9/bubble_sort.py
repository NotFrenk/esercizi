# ASYMPTOTIC NOTATION & BUBBLE SORT

"""ORIGINALE"""
def bubble_sorte(x:list[float]):
    for i in range(len(x)):
        for j in  range(len(x) - 1):
            if x[j] > x[j + 1]:
                temp: float= x[j + 1]
                x[j + 1] = x[j]
                x[j] = x[j + 1]
                

"""MIGLIORAMENTO"""
# linea 17
def bubble_sorte_migliorato(x:list[float]):
    for i in range(len(x)):
        for j in  range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                temp: float= x[j + 1]
                x[j + 1] = x[j]
                x[j] = x[j + 1]