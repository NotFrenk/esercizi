from flask import Flask, json, request
from myjson import SerializaJson, DeserializeJson

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
   #prendi i dati della richiesta
   content_type = request.headers.get('Content-Type')
   print("Ricevuta chiamata " + content_type)
   if content_type=="application/json":
      jRequest = request.json
      sCodiceFiscale=jRequest["codice fiscale"]
      print("ricevuto" + sCodiceFiscale)

      #carichiamo l'anagrafe
      dAnagrafe = DeserializeJson(sFileAnagrafe)
      if sCodiceFiscale not in dAnagrafe:
         dAnagrafe[sCodiceFiscale] = jRequest
         jResponse = {"Error":"000", "Msg":"ok"}
         return json.dumps(jResponse),200
      else:
         jResponse = {"Error":"001", "Msg":"codice fiscale gia esistente"}
         return json.dumps(jResponse),200
   else:
      return "Errore, formato non riconosciuto",401

api.run(host="127.0.0.1", port=8080)
   #controlla che il cittadino non è gia presente in anagrafe