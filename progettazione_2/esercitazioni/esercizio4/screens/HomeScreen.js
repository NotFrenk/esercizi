import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import Styles from './Styles';

const HomeScreen = ({ navigation }) => {
  return (
    <View style={Styles.container}>
      <Text style={Styles.title}>Benvenuto nell'App</Text>
      <TouchableOpacity 
        style={Styles.button}
        onPress={() => navigation.navigate('Registration')}
      >
        <Text style={Styles.buttonText}>Vai alla Registrazione</Text>
      </TouchableOpacity>
    </View>
  );
};

export default HomeScreen;