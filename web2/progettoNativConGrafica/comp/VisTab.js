import React from "react";
import { View, Text, ScrollView, StyleSheet } from "react-native";

const RisultatiTable = ({ data }) => {  return (
    <ScrollView horizontal>
      <ScrollView style={styles.scrollContainer}>
        <View style={styles.tableContainer}>
          {/* Intestazione */}
          <View style={[styles.row, styles.headerRow]}>
            <Text style={[styles.cell, styles.headerCell]}>ID</Text>
            <Text style={[styles.cell, styles.headerCell]}>Compagnia</Text>
            <Text style={[styles.cell, styles.headerCell]}>Prezzo (€)</Text>
          </View>

          {/* Contenuto della tabella */}
          {data.map((item, index) => (
            <View key={index} style={styles.row}>
              <Text style={styles.cell}>{item[0]}</Text>
              <Text style={styles.cell}>{item[1]}</Text>
              <Text style={styles.cell}>{item[2]}€</Text>
            </View>
          ))}
        </View>
      </ScrollView>
    </ScrollView>
  );
};

// Stili
const styles = StyleSheet.create({
  scrollContainer: {
    maxHeight: 300, // Imposta un limite di altezza per evitare che la tabella cresca all'infinito
  },
  tableContainer: {
    backgroundColor: "rgba(0, 0, 0, 0.8)",
    borderRadius: 10,
    padding: 10,
    width: 300, // Imposta una larghezza fissa per evitare compressione
    marginTop: 15,
  },
  row: {
    flexDirection: "row",
    borderBottomWidth: 1,
    borderBottomColor: "white",
    paddingVertical: 8,
  },
  headerRow: {
    borderBottomWidth: 2,
  },
  cell: {
    flex: 1,
    textAlign: "center",
    color: "white",
    fontSize: 16,
    paddingHorizontal: 5,
  },
  headerCell: {
    fontWeight: "bold",
  },
});

 export default RisultatiTable;