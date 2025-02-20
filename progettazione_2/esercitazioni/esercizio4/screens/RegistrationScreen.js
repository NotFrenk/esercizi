import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
} from 'react-native';
import Styles from './Styles';

const RegistrationScreen = ({ navigation }) => {
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    email2: '',
    telefono: '',
    password: '',
  });

  const [errors, setErrors] = useState({
    nome: '',
    email: '',
    email2: '',
    telefono: '',
    password: '',
  });

  const validateForm = () => {
    let isValid = true;
    const newErrors = {};

    // Validazione nome
    if (!formData.nome.trim()) {
      newErrors.nome = 'Il nome è obbligatorio';
      isValid = false;
    } else if (formData.nome.length < 2) {
      newErrors.nome = 'Il nome deve essere di almeno 2 caratteri';
      isValid = false;
    }

    // Validazione email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email.trim()) {
      newErrors.email = "L'email è obbligatoria";
      isValid = false;
    } else if (!emailRegex.test(formData.email)) {
      newErrors.email = 'Inserisci un indirizzo email valido';
      isValid = false;
    } else if (formData.email2 !== formData.email){
      newErrors.email2 = 'Le due email devono essere uguali';
      isValid = false;
    }

    // Validazione telefono
    const phoneRegex = /^[0-9]{10}$/;
    if (!formData.telefono.trim()) {
      newErrors.telefono = 'Il telefono è obbligatorio';
      isValid = false;
    } else if (!phoneRegex.test(formData.telefono)) {
      newErrors.telefono = 'Inserisci un numero di telefono valido (10 cifre)';
      isValid = false;
    }

    // Validazione password
    if (!formData.password) {
      newErrors.password = 'La password è obbligatoria';
      isValid = false;
    } else if (formData.password.length < 6) {
      newErrors.password = 'La password deve essere di almeno 6 caratteri';
      isValid = false;
    }

    setErrors(newErrors);
    return isValid;
  };

  const handleSubmit = () => {
    if (validateForm()) {
      navigation.navigate('Success');
    }
  };

  return (
    <ScrollView style={Styles.container}>
      <View style={Styles.formContainer}>
        <View style={Styles.inputGroup}>
          <Text style={Styles.label}>Nome</Text>
          <TextInput
            style={[Styles.input, errors.nome && Styles.inputError]}
            value={formData.nome}
            onChangeText={(text) => setFormData({ ...formData, nome: text })}
            placeholder="Inserisci il tuo nome"
          />
          {errors.nome && <Text style={Styles.errorText}>{errors.nome}</Text>}
        </View>

        <View style={Styles.inputGroup}>
          <Text style={Styles.label}>Email</Text>
          <TextInput
            style={[Styles.input, errors.email && Styles.inputError]}
            value={formData.email}
            onChangeText={(text) => setFormData({ ...formData, email: text })}
            placeholder="Inserisci la tua email"
            keyboardType="email-address"
            autoCapitalize="none"
          />
          {errors.email && <Text style={Styles.errorText}>{errors.email}</Text>}
        </View>

        <View style={Styles.inputGroup}>
          <Text style={Styles.label}>Email</Text>
          <TextInput
            style={[Styles.input, errors.email2 && Styles.inputError]}
            value={formData.email2}
            onChangeText={(text) => setFormData({ ...formData, email2: text })}
            placeholder="Inserisci nuovamente la tua email"
            keyboardType="email-address"
            autoCapitalize="none"
          />
          {errors.email2 && <Text style={Styles.errorText}>{errors.email2}</Text>}
        </View>

        <View style={Styles.inputGroup}>
          <Text style={Styles.label}>Telefono</Text>
          <TextInput
            style={[Styles.input, errors.telefono && Styles.inputError]}
            value={formData.telefono}
            onChangeText={(text) => setFormData({ ...formData, telefono: text })}
            placeholder="Inserisci il tuo numero di telefono"
            keyboardType="phone-pad"
          />
          {errors.telefono && <Text style={Styles.errorText}>{errors.telefono}</Text>}
        </View>

        <View style={Styles.inputGroup}>
          <Text style={Styles.label}>Password</Text>
          <TextInput
            style={[Styles.input, errors.password && Styles.inputError]}
            value={formData.password}
            onChangeText={(text) => setFormData({ ...formData, password: text })}
            placeholder="Inserisci la tua password"
            secureTextEntry
          />
          {errors.password && <Text style={Styles.errorText}>{errors.password}</Text>}
        </View>

        <TouchableOpacity style={Styles.button} onPress={handleSubmit}>
          <Text style={Styles.buttonText}>Registrati</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
};
export default RegistrationScreen;