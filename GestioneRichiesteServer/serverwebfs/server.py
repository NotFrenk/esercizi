from flask import Flask, render_template

api = Flask(__name__)

utenti = [['mario', 'rossi', 'M','0'],['gianni', 'derossi', 'M','0'], ['Anita', 'Garibaldi', 'F','0']]


@api.route('/', methods=['GET'])
def index():
   return render_template('index.html')

@api.route('/regok', methods=['GET'])
def regOk():
   return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def regKo():
   return render_template('reg_ko.html')

@api.route('/registrati', methods=['GET'])
def registra():
   nome = request.args.get("nome")
   print ("nome inserito" + nome)

   password = request.args.get("cognome")
    


   return render_template('reg_ko.html')

api.run(host="0.0.0.0", port=8085)
