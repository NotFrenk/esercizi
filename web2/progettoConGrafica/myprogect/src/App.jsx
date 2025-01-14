import React, { useEffect, useState } from "react";

const App = () => {
    const [aeroporti, setAeroporti] = useState([]); // Stato per i dati degli aeroporti
    const [error, setError] = useState(null);       // Stato per gli errori

    useEffect(() => {
        // Chiamata API usando fetch
        fetch('http://localhost:5001/aeroporti')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Errore nella richiesta: ${response.statusText}`);
                }
                return response.json();
            })
            .then(data => {
                setAeroporti(data.risultato); // Imposta i dati degli aeroporti nello stato
            })
            .catch(err => {
                setError(err.message); // Imposta l'errore nello stato
            });
    }, []); // Esegui solo al montaggio del componente

    return (
        <div>
            <h1>Aeroporti</h1>
            {error && <p style={{ color: "red" }}>Errore: {error}</p>}
            <ul>
                {aeroporti.map((aeroporto, index) => (
                    <li key={index}>{JSON.stringify(aeroporto)}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;
