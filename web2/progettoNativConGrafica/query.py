import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

# Configurazione del database
DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
}

# # Connessione al database
# def get_db_connection():
#     try:
#         connection = psycopg2.connect(**DB_CONFIG)
#         print("Connessione riuscita al database")
#         return connection
#     except Exception as e:
#         print(f"Errore durante la connessione al database: {e}")
#         raise

# # Eseguire una query sul database
# def read_db(connection, query):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query)
#         rows = cursor.fetchall()
#         return rows
#     except Exception as e:
#         raise e
#     finally:
#         cursor.close()

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


@app.route('/aeroporti', methods=['GET'])
def aeroporti():
    # Elenco Aeroporti
    return jsonify(

{'risultato': [('JFK', 'JFK Airport', '300'), 
                ('FCO', 'Aeroporto di Roma Fiumicino', '499.99'), 
                ('CIA', 'Aeroporto di Roma Ciampino', '170'), 
                ('CDG', 'Charles de Gaulle, Aeroport de Paris', '278'), 
                ('HTR', 'Heathrow Airport, London', '300'), 
                ('GER', 'AE Ger', '600')]}
)
#@app.route('/aeroporti')
# def aeroporti():
#     try:
#         connection = get_db_connection()
#         query = "SELECT * FROM aeroporto"
#         results = read_db(connection, query)
#         return jsonify({'risultato': results})
#     except Exception as e:
#         return jsonify({'errore': str(e)}), 500
#     finally:
#         connection.close()

@app.route('/vol.sopra.med')
def y():
    # Elenco Aeroporti
    return jsonify(

{'risultato': [('JFK', 'JFK Airport', '300'), 
                ('FCO', 'Aeroporto di Roma Fiumicino', '499.99'), 
                ('CIA', 'Aeroporto di Roma Ciampino', '170'), 
                ('CDG', 'Charles de Gaulle, Aeroport de Paris', '278'), 
                ('HTR', 'Heathrow Airport, London', '300'), 
                ('GER', 'AE Ger', '600')]}
    )
# def voli_sopra_media():
#     try:
#         connection = get_db_connection()
#         query = """
#         SELECT V.codice, V.comp, V.durataMinuti 
#         FROM volo V 
#         WHERE V.durataMinuti > (
#             SELECT AVG(v2.durataMinuti) 
#             FROM volo v2 
#             WHERE v2.comp = V.comp)
#         """
#         results = read_db(connection, query)
#         return jsonify({'risultato': results})
#     except Exception as e:
#         return jsonify({'errore': str(e)}), 500
#     finally:
#         connection.close()

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



























# import React, { useState } from "react";
# import {
#   View,
#   Text,
#   TouchableOpacity,
#   StyleSheet,
#   ImageBackground,
#   ActivityIndicator,
#   Platform
# } from "react-native";
# import RisultatiTable from "./comp/VisTab";

# const API_BASE_URL = Platform.OS === "android" ? "http://10.0.2.2:5001" : "http://127.0.0.1:5001";

# const App = () => {
#   const [risultato, setRisultato] = useState(null);
#   const [error, setError] = useState(null);
#   const [loading, setLoading] = useState(false);

#   const fetchQuery = async (endpoint) => {
#     setLoading(true);
#     setError(null);
#     setRisultato(null);

#     try {
#       const response = await fetch(`${API_BASE_URL}${endpoint}`);
#       if (!response.ok) {
#         throw new Error(`Errore: ${response.statusText}`);
#       }
#       const data = await response.json();
#       setRisultato(data.risultato);
#     } catch (err) {
#       setError(err.message);
#     } finally {
#       setLoading(false);
#     }
#   };


#   return (
#     <ImageBackground source={require("./assets/immaginehometop.png")} style={styles.background}>
#       <View style={styles.container}>
#         <Text style={styles.header}>Cerca il tuo prossimo volo</Text>
#         <View style={styles.nav}>
#           {["/aeroporti", "/vol.sopra.med", "/serv.api"].map((endpoint, index) => (
#             <TouchableOpacity key={index} style={styles.button} onPress={() => fetchQuery(endpoint)}>
#               <Text style={styles.buttonText}>{
#                 endpoint === "/aeroporti" ? "Visualizza Aeroporti" :
#                 endpoint === "/vol.sopra.med" ? "Voli Sopra la Media" :
#                 "Città Servite da Apitalia"
#               }</Text>
#             </TouchableOpacity>
#           ))}
#         </View>

#         {loading && <ActivityIndicator size="large" color="#fff" style={styles.loader} />}
#         {error && <Text style={styles.error}>Errore: {error}</Text>}
        
#         {risultato && <RisultatiTable data={risultato} />}
#       </View>
#     </ImageBackground>
#   );
# };


# const styles = StyleSheet.create({
#   background: {
#     flex: 1,
#     resizeMode: "cover",
#     justifyContent: "center",
#     alignItems: "center",
#     overflow:"scroll",
#   },
#   container: {
#     padding: 20,
#     alignItems: "center",
#   },
#   header: {
#     fontSize: 28,
#     fontWeight: "bold",
#     color: "rgba(0, 56, 240, 0.8)",
#     marginBottom: 20,
#     textShadowColor: "rgba(0, 0, 0, 0.8)",
#     textShadowOffset: { width: 1, height: 1 },
#     textShadowRadius: 5,
#   },
#   nav: {
#     flexDirection: "row",
#     justifyContent: "center",
#     flexWrap: "wrap",
#     marginBottom: 20,
#   },
#   button: {
#     backgroundColor: "rgba(255, 255, 255, 0.9)",
#     padding: 12,
#     margin: 5,
#     borderRadius: 15,
#     shadowColor: "#000",
#     shadowOffset: { width: 0, height: 2 },
#     shadowOpacity: 0.3,
#     shadowRadius: 4,
#     elevation: 5,
#   },
#   buttonText: {
#     fontSize: 16,
#     fontWeight: "bold",
#     color: "#333",
#   },
#   loader: {
#     marginTop: 20,
#   },
#   error: {
#     color: "#ff4d4d",
#     fontWeight: "bold",
#     fontSize: 16,
#     marginTop: 20,
#     textAlign: "center",
#   },
#   resultContainer: {
#     backgroundColor: "rgba(0, 0, 0, 0.8)",
#     padding: 10,
#     borderRadius: 10,
#     width: "90%",
#     marginTop: 15,
#   },

# });

# export default App;