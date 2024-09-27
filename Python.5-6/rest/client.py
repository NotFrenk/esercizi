import json, requests, sys

base_url = "http://127.0.0.1:8080"

def RichiediDatiCittadino():
   nome = input("inserisci il tuo nome: ")
   cognome = input("inserisci il tuo cognone: ")
   dataNascita = input("iserisi data di nascita: ")
   codFiscale = input("inserisci codice fiscale: ")
   jRequest = {"nome":nome, "cognome":cognome, "dataNascita":dataNascita, "codFiscale":codFiscale}
   return jRequest

def ModificaDatiCittadino():
   MODnome = input("inserisci il tuo nome: ")
   MODcognome = input("inserisci il tuo cognone: ")
   MODdataNascita = input("iserisi data di nascita: ")
   MODcodFiscale = input("inserisci codice fiscale: ")
   jRequest = {"nome":MODnome, "cognome":MODcognome, "dataNascita":MODdataNascita, "codFiscale":MODcodFiscale}
   return jRequest

def EliminaCittadino():
   pass

def CreaInterfaccia():
   print("operazioni disponibili:")
   print("1. Inserisci cittadino (es. atto di nascita)")
   print("2. Richiedi dati cittadino (es. cert. residenza)")
   print("3. Modifica dati cittadino")
   print("4. Elimina cittadino")
   print("5. Exit")

CreaInterfaccia()
sOper = input("seleziona operazione")
while (sOper != "5"):

   if sOper=="1":
      api_url=base_url + "/add_cittadino"
      jsonDataRequest = RichiediDatiCittadino()
      try:
         response = requests.post(api_url,json=jsonDataRequest)
         print(response.status_code)
         print(response.headers["Content-Type"])
         data1 = response.json()
         print(data1)

      except:
         print("Problemi di comunicazione con il server, riprovi piu tardi")

   CreaInterfaccia()
   sOper = input("Seleziona operazione")




sys.exit()