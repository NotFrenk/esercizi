import React from 'react';
import styles from '../styles';
import { View, Text } from 'react-native';

const ProductDetailsScreen = ({ route }) => {
  const { productId } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Dettagli Prodotto {productId}</Text>
      <Text style={styles.description}>
        Questo è un esempio di pagina dettaglio prodotto.
        Qui puoi aggiungere tutte le informazioni relative al prodotto selezionato.
      </Text>
    </View>
  );
}

export default ProductDetailsScreen;