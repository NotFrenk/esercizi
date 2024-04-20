def add_one(n:int):
    return n + 1
#res=add_one(3)
print(add_one(10))

def add_one_to_list(l=list):
    nuova_lista:list=[] 
    for i in l:
        nuova_lista.append(add_one(i))
    print(nuova_lista)
add_one_to_list([1,2,3])