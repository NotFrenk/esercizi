from flask import Flask, render_template, request

api = Flask(__name__)

utenti: list[list[str]] = [['Mario','Aa@12345','1','Roma','0'],
                           ['Luigi','Bb$23456','1','Pescara','0'],
                           ['Francesca','Cc!34567','2','Milano','0']]

@api.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')


@api.route('/regok', methods=['GET'])
def reg_ok():
    
    return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def reg_ko():
    
    return render_template('reg_ko.html')

@api.route('/registrati', methods=['GET'])
def registra():
    utente: list[str] = [str(request.args.get("fname")),
                         str(request.args.get("fpassword")), 
                         str(request.args.get("fsesso")), 
                         str(request.args.get("fComune")),
                         b'0']
    #print(utente)

    #Devo prendere tutti i dati e verificare se la terna c'è nel vettore degli utenti

    if(utente in utenti):
        ind: int = utenti.index(utente)

        utenti[ind][4] = '1'
        return render_template('reg_ok.html')
    else:
        return render_template('reg_ko.html')
    


api.run(host='0.0.0.0',port=8085)