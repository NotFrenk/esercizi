import React, { useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  FlatList,
  StyleSheet,
  ImageBackground,
  ActivityIndicator,
  Platform
} from "react-native";

const API_BASE_URL = Platform.OS === "android" ? "http://10.0.2.2:5001" : "http://127.0.0.1:5001";

const App = () => {
  const [risultato, setRisultato] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchQuery = (endpoint) => {
    setLoading(true);
    console.log(`Chiamata API: ${endpoint}`);


    fetch(`${API_BASE_URL}${endpoint}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Errore: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => {
        setRisultato(data.risultato);
        setError(null);
      })
      .catch((err) => {
        setError(err.message);
        setRisultato(null);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  return (
    <ImageBackground source={require("./assets/immaginehometop.png")} style={styles.background}>
      
      <View style={styles.container}>
        <Text style={styles.header}>Cerca il tuo prossimo volo</Text>

        <View style={styles.nav}>
          <TouchableOpacity style={styles.button} onPress={() => fetchQuery("/aeroporti")}>
            <Text style={styles.buttonText}>Visualizza Aeroporti</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={() => fetchQuery("/vol.sopra.med")}>
            <Text style={styles.buttonText}>Voli Sopra la Media</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={() => fetchQuery("/serv.api")}>
            <Text style={styles.buttonText}>Città Servite da Apitalia</Text>
          </TouchableOpacity>
        </View>

        {loading && <ActivityIndicator size="large" color="#fff" style={styles.loader} />}

        {error && <Text style={styles.error}>Errore: {error}</Text>}

        {risultato && (
          <View style={styles.resultContainer}>
            <Text style={styles.resultTitle}>Risultato:</Text>
            <FlatList
              data={risultato}
              keyExtractor={(item, index) => index.toString()}
              renderItem={({ item }) => (
                <View style={styles.resultItem}>
                  <Text style={styles.bold}>ID:</Text> {item[0]}{"\n"}
                  <Text style={styles.bold}>Compagnia:</Text> {item[1]}{"\n"}
                  <Text style={styles.bold}>Prezzo:</Text> {item[2]}€
                </View>
              )}
            />
          </View>
        )}
      </View>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  background: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center",
    alignItems: "center",
  },

  container: {
    padding: 20,
    alignItems: "center",
  },
  header: {
    fontSize: 28,
    fontWeight: "bold",
    color: "white",
    marginBottom: 20,
    textShadowColor: "rgba(0, 0, 0, 0.8)",
    textShadowOffset: { width: 1, height: 1 },
    textShadowRadius: 5,
  },
  nav: {
    flexDirection: "row",
    justifyContent: "center",
    flexWrap: "wrap",
    marginBottom: 20,
  },
  button: {
    backgroundColor: "rgba(255, 255, 255, 0.9)",
    padding: 12,
    margin: 5,
    borderRadius: 15,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    elevation: 5,
  },
  buttonText: {
    fontSize: 16,
    fontWeight: "bold",
    color: "#333",
  },
  loader: {
    marginTop: 20,
  },
  error: {
    color: "#ff4d4d",
    fontWeight: "bold",
    fontSize: 16,
    marginTop: 20,
    textAlign: "center",
  },
  resultContainer: {
    backgroundColor: "rgba(0, 0, 0, 0.8)",
    padding: 15,
    borderRadius: 10,
    width: "90%",
    marginTop: 15,
  },
  resultTitle: {
    fontSize: 20,
    fontWeight: "bold",
    color: "white",
    marginBottom: 10,
    textAlign: "center",
  },
  resultItem: {
    backgroundColor: "rgba(255, 255, 255, 0.2)",
    padding: 10,
    marginVertical: 5,
    borderRadius: 8,
    color: "white",
  },
  bold: {
    fontWeight: "bold",
    color: "white",
  },
});


export default App;
