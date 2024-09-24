#Scrivere in python due procedure, 
#la prima che, se riceve come parametro mylist1 da come valore di ritorno mylist2.
#La seconda che, se riceve come parametro mylist2 da come valore di ritorno mylist1.

import ast

lista_1 = "['mario', 'gino', 'lucrezia']"
lista_2 = ['mario', 'gino', 'lucrezia']

def DeserializzaLista (lista_1):
   return ast.literal_eval(lista_1)

print(type(DeserializzaLista(lista_1)))
print(DeserializzaLista(lista_1))

def SerializzaLista (lista_2):
   return str(lista_2)

print(type(DeserializzaLista(lista_2)))
print(DeserializzaLista(lista_2))


