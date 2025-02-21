import React, { useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  ImageBackground,
  ActivityIndicator,
  Platform,
  ScrollView
} from "react-native";
import RisultatiTable from "./comp/VisTab";

const API_BASE_URL = Platform.OS === "android" ? "http://10.0.2.2:5001" : "http://127.0.0.1:5001";

const App = () => {
  const [risultato, setRisultato] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchQuery = async (endpoint) => {
    setLoading(true);
    setError(null);
    setRisultato(null);

    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`);
      if (!response.ok) {
        throw new Error(`Errore: ${response.statusText}`);
      }
      const data = await response.json();
      setRisultato(data.risultato);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ImageBackground source={require("./assets/immaginehometop.png")} style={styles.background}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.container}>
          <Text style={styles.header}>Cerca il tuo prossimo volo</Text>
          <View style={styles.nav}>
            {["/aeroporti", "/vol.sopra.med", "/serv.api"].map((endpoint, index) => (
              <TouchableOpacity key={index} style={styles.button} onPress={() => fetchQuery(endpoint)}>
                <Text style={styles.buttonText}>{
                  endpoint === "/aeroporti" ? "Visualizza Aeroporti" :
                  endpoint === "/vol.sopra.med" ? "Voli Sopra la Media" :
                  "Città Servite da Apitalia"
                }</Text>
              </TouchableOpacity>
            ))}
          </View>

          {loading && <ActivityIndicator size="large" color="#fff" style={styles.loader} />}
          {error && <Text style={styles.error}>Errore: {error}</Text>}

          {risultato && <RisultatiTable data={risultato} />}
        </View>
      </ScrollView>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  background: {
    flex: 1, // Riempie tutto lo schermo
    width: "100%", // Evita lo scorrimento orizzontale
    height: "100%", // Si adatta all'altezza dello schermo
    resizeMode: "cover", // Mantiene l'immagine proporzionata
  },
  scrollContainer: {
    flexGrow: 1, // Permette lo scroll verticale senza spazi bianchi
    paddingTop: "38%",
  },
  container: {
    flex: 1, // Riempie tutto lo spazio disponibile
    padding: 20,
    alignItems: "center",
  },
  header: {
    fontSize: 28,
    fontWeight: "bold",
    color: "rgba(0, 56, 240, 0.8)",
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
});

export default App;