#Scrivere in python due procedure, 
#la prima che, se riceve come parametro mylist1 da come valore di ritorno mylist2.
#La seconda che, se riceve come parametro mylist2 da come valore di ritorno mylist1.
"""import ast

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
"""
import json

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"


def SerializaJson(dData,file_path):
   try:
      with open(file_path, 'w') as file:
         json.dump(dData,file)
         return True
   except Exception as e:
        print(f"Errore durante la serializzazione: {e}")
        return False


def DeserializeJson(file_path):
   try:
        with open(file_path, 'r') as file:
           return json.load(file)
   except Exception as e:
        print(f"Errore durante la deserializzazione: {e}")
        return None

file_path="data.json"

if SerializaJson(mydict_1,file_path):
   print("Serializzazione riuscita!")

dict_from_file = DeserializeJson(file_path)
if dict_from_file is not None:
   print("Deserializzazione riuscita!")
   print(dict_from_file)