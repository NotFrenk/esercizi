import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

# Configurazione del database
DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "cielo",
    "user": "postgres",
    "password": "postgres",
}

# Connessione al database
def get_db_connection():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        print("Connessione riuscita al database")
        return connection
    except Exception as e:
        print(f"Errore durante la connessione al database: {e}")
        raise

# Eseguire una query sul database
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

# Creazione dell'app Flask
app = Flask(__name__)
CORS(app)  # Abilita il CORS per consentire richieste dal frontend React

# Rotte API
@app.route('/')
def home():
    return """
    <h1>Benvenuto nella nostra libreria!</h1>
    <p>Usa <a href='/aeroporti'>/aeroporti</a> per visualizzare tutti gli aeroporti.</p>
    <p>Usa <a href='/vol.sopra.med'>/vol.sopra.med</a> per visualizzare i voli con durata sopra la media per compagnia.</p>
    <p>Usa <a href='/serv.api'>/serv.api</a> per visualizzare le città servite da più di un aeroporto per Apitalia.</p>
    <p>Usa <a href='/personalizzata'>/personalizzata</a> per eseguire una query personalizzata.</p>
    """

@app.route('/aeroporti')
def aeroporti():
    try:
        connection = get_db_connection()
        query = "SELECT * FROM aeroporto"
        results = read_db(connection, query)
        return jsonify({'risultato': results})
    except Exception as e:
        return jsonify({'errore': str(e)}), 500
    finally:
        connection.close()

@app.route('/vol.sopra.med')
def voli_sopra_media():
    try:
        connection = get_db_connection()
        query = """
        SELECT V.codice, V.comp, V.durataMinuti 
        FROM volo V 
        WHERE V.durataMinuti > (
            SELECT AVG(v2.durataMinuti) 
            FROM volo v2 
            WHERE v2.comp = V.comp)
        """
        results = read_db(connection, query)
        return jsonify({'risultato': results})
    except Exception as e:
        return jsonify({'errore': str(e)}), 500
    finally:
        connection.close()

@app.route('/serv.api')
def cita_apitalia():
    try:
        connection = get_db_connection()
        query = """
        SELECT l.citta
        FROM LuogoAeroporto l
        JOIN Aeroporto a ON l.aeroporto = a.codice
        JOIN ArrPart ap ON a.codice = ap.partenza OR a.codice = ap.arrivo
        WHERE ap.comp = 'Apitalia'
        GROUP BY l.citta 
        HAVING COUNT(DISTINCT l.aeroporto) > 1
        """
        results = read_db(connection, query)
        return jsonify({'risultato': results})
    except Exception as e:
        return jsonify({'errore': str(e)}), 500
    finally:
        connection.close()

@app.route('/personalizzata', methods=['POST'])
def crea_query():
    print("Metodo ricevuto:", request.method)
    try:
        data = request.get_json()
        query = data.get('query')
        print("Ricevuto:", data)
        print("Query:", query)

        if not query:
            return jsonify({'errore': 'Nessuna query fornita'}), 400

        connection = get_db_connection()
        results = read_db(connection, query)

        print("risultati ottenuti:", results)

        return jsonify({'risultato': results})
    except Exception as e:

        print("Errore nel backend:", str(e))
        return jsonify({'errore': str(e)}), 500
    finally:
        if 'connection' in locals() and connection:
            connection.close()

# Avvio del server Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
