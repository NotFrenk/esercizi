import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const FormScreen = ({ navigation }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [nameFocus, setNameFocus] = useState(false);  // Stato per il focus su "Name"
  const [emailFocus, setEmailFocus] = useState(false);  // Stato per il focus su "Email"


  const handleSubmit = () => {
    navigation.navigate('Details', { name, email });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Form Screen</Text>
      <TextInput
        style={styles.input}
        placeholder="Name"
        value={name}
        onChangeText={setName}
        onFocus={() => setNameFocus(true)}  // Attiva focus
        onBlur={() => setNameFocus(false)}  // Disattiva focus
        placeholderTextColor={nameFocus ? 'transparent' : 'gray'}  // Cambia il colore del placeholder
    
      />
      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        onFocus={() => setEmailFocus(true)}  // Attiva focus
        onBlur={() => setEmailFocus(false)}  // Disattiva focus
        placeholderTextColor={emailFocus ? 'transparent' : 'gray'}  // Cambia il colore del placeholder
      />
      <Button title="Submit" onPress={handleSubmit} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  input: {
    width: '80%',
    padding: 10,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: 'blue',
    borderRadius: 5,
  },
});

export default FormScreen;