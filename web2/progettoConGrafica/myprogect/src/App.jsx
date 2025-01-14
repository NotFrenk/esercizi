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
        <div style={{ padding: "20px"}}>
          <h1>Gestione Query</h1>
          <div>
            <button onClick={() => fetchQuery('/aeroporti')}>Visualizza aeroporti</button>
            <button onClick={() => fetchQuery('/vol.sopra.med')}>Voli sopra la media</button>
            <button onClick={() => fetchQuery('/serv.api')}>Città servite da apitalia</button>
          </div>
          <div style={{ marginTop: "20px"}}>
            <h2>Query personalizata</h2>
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Scrivi una query SQL"
              style={{width: "300px", marginRight: "10px"}}
            />
            <button onClick={sendCustomQuery}>Esegui Query</button>
          </div>
          <div style={{marginTop: "20"}}>
            {error && <p style={{color: "red"}}> Errore: {error}</p>}
            {risultato && (
              <div>
                <h2>Risultato:</h2>
                <ul>
                  {risultato.map((item, index) => (
                    <li key = {index}>{JSON.stringify(item)}</li>
                  ))}
                </ul>
          </div>
            )}

export default App;
