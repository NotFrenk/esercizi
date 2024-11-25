
import psycopg2
import time 
from flask import Flask, jsonify, request

host = "localhost"
port = "5432"
dbname = "cielo"
user = "postgres"
password = "postgres"

try:
    connection = psycopg2.connect(
        host=host, 
        port=port, 
        dbname=dbname, 
        user=user, 
        password=password
    )
    print("Connessione riuscita al database")
except Exception as e:
    print(f"Errore durante l'esecuzione del programma: {e}")

def read_db(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise e
    finally:
        cursor.close()



def query_interactive():
    print("\n--- Modalità Query Personalizzata ---")
    print("Scrivi la tua query SQL : ")
    while True:
        custom_query = input("SQL> ")
        if custom_query.lower() == 'exit':
            print("Uscita dalla modalità interattiva.")
            break
        try:
            cursor = connection.cursor()
            cursor.execute(custom_query)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Errore nell'esecuzione della query: {e}")






app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Benvenuto nella nostra libreria!</h1>
    <p>Usa <a href='/aeroporti'>/aeroporti</a> per visualizzare tutti gli aeroporti</p>
    <p>Usa <a href='/vol.sopra.med'>/vol.sopra.med</a> per visualizzare i voli con durata sopra la media per compagnia</p>
    <p>Usa <a href='/serv.api'>/serv.api</a> per visualizzare le città servite da più di un aeroporto per Apitalia</p>
    <p>Usa <a href='/personalizata'>/personalizata</a> per Scrivere una query personalizzata</p>
    """

@app.route('/aeroporti')
def aeroporti():
   retQuery = read_db(connection, "SELECT * FROM aeroporto")
   return jsonify({'risultato' : retQuery})

@app.route('/vol.sopra.med')
def voli_sopra_media():
    retQuery = read_db(connection, 
        """        
        SELECT V.codice, V.comp, V.durataMinuti 
        FROM volo V 
        WHERE V.durataMinuti > (
            SELECT AVG(v2.durataMinuti) 
            FROM volo v2 
            WHERE v2.comp = V.comp)""" 
        )
    return jsonify({'risultato' : retQuery})

@app.route('/serv.api')
def cita_apitalia():
    retQuery = read_db(connection, 
        """
        SELECT l.citta
        FROM LuogoAeroporto l
        JOIN Aeroporto a ON l.aeroporto = a.codice
        JOIN ArrPart ap ON a.codice = ap.partenza OR a.codice = ap.arrivo
        WHERE ap.comp = 'Apitalia'
        GROUP BY l.citta 
        HAVING COUNT(DISTINCT l.aeroporto) > 1""")
    return jsonify({'risultato' : retQuery})

@app.route('/personalizata')
def crea_query():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)



