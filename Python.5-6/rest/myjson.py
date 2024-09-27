import json
import jsonschema
import requests
import sys

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