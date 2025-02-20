import React from 'react';
import { View, Text, TouchableOpacity} from 'react-native';
import Styles from './Styles';

const SuccessScreen = ({ navigation }) => {
  return (
    <View style={Styles.container}>
      <Text style={Styles.title}>Registrazione Completata!</Text>
      <Text style={Styles.message}>
        La tua registrazione è stata completata con successo.
      </Text>
      <TouchableOpacity 
        style={Styles.button}
        onPress={() => navigation.navigate('Home')}
      >
        <Text style={Styles.buttonText}>Torna alla Home</Text>
      </TouchableOpacity>
    </View>
  );
};
export default SuccessScreen;