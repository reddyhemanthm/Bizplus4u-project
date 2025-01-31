npx react-native init SecureLoginApp
cd SecureLoginApp 
npm install axios
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import axios from 'axios';

const LoginScreen = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        try {
            const response = await axios.post('http://your-server-url/login', { email, password });
            if (response.data.success) {
                Alert.alert('Login Successful', 'Welcome!');
            } else {
                Alert.alert('Login Failed', response.data.message);
            }
        } catch (error) {
            Alert.alert('Error', 'Something went wrong. Please try again later.');
        }
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Login</Text>
            <TextInput
                style={styles.input}
                placeholder="Email"
                value={email}
                onChangeText={setEmail}
                keyboardType="email-address"
                autoCapitalize="none"
            />
            <TextInput
                style={styles.input}
                placeholder="Password"
                value={password}
                onChangeText={setPassword}
                secureTextEntry
            />
            <Button title="Login" onPress={handleLogin} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        padding: 16,
    },
    title: {
        fontSize: 24,
        marginBottom: 24,
        textAlign: 'center',
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 12,
        paddingHorizontal: 8,
    },
});

export default LoginScreen;
import React from 'react';
import LoginScreen from './components/LoginScreen';

const App = () => {
    return <LoginScreen />;
};

export default App;
mkdir backend
cd backend
npm init -y
npm install express body-parser bcrypt jsonwebtoken
const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const app = express();
const PORT = 3000;
const SECRET_KEY = 'your-secret-key'; // Replace with a secure secret key

// Middleware
app.use(bodyParser.json());

// Dummy users data
const users = [
    { id: 1, email: 'user@example.com', password: bcrypt.hashSync('password123', 10) }
];

// Login Route
app.post('/login', (req, res) => {
    const { email, password } = req.body;
    const user = users.find(u => u.email === email);

    if (user && bcrypt.compareSync(password, user.password)) {
        const token = jwt.sign({ id: user.id, email: user.email }, SECRET_KEY, { expiresIn: '1h' });
        res.json({ success: true, token });
    } else {
        res.json({ success: false, message: 'Invalid email or password' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
node server.js
npx react-native run-android  # For Android
npx react-native run-ios      # For iOS
