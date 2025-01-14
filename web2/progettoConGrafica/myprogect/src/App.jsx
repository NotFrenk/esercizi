import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
    const [aeroporti, setAeroporti] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Chiamata all'API Flask
        axios.get('http://localhost:5001/aeroporti')
            .then(response => {
                setAeroporti(response.data.risultato);
            })
            .catch(err => {
                setError(err.message);
            });
    }, []);

    return (
        <div>
            <h1>Aeroporti</h1>
            {error && <p>Errore: {error}</p>}
            <ul>
                {aeroporti.map((aeroporto, index) => (
                    <li key={index}>{JSON.stringify(aeroporto)}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;
