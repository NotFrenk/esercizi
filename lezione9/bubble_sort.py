# ASYMPTOTIC NOTATION & BUBBLE SORT

def bubble_sorte(x:list[float])
    for i in range(len(x)):
        for j in  range(len(x) - 1):
            if x[j] > x[j + 1]:
                temp: float= x[j + 1]
                x[j + 1] = x[j]
                x[j] = x[j + 1]
                


