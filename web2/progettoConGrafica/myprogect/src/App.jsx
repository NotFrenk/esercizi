import React,{useState, useEffect} from "react";
import axios from "axios";
import "./App.css";


const App = () => {
  const [risultato, setRisultato] = useState(null);
  const [error, setError] = useState(null);
  
  const fetchQuery = (endpoint) => {
      fetch(`http://localhost:5001${endpoint}`)
          .then(response => {
              if (!response.ok) {
                  throw new Error(`Errore nella richiesta: ${response.statusText}`);
              }
              return response.json();
          })
          .then(data => {
              setRisultato(data.risultato);
              setError(null);
          })
          .catch(err => {
              setError(err.message);
              setRisultato(null);
          });
  };


return (
    <div className="app-container">
      <header className="app-header">
        <h1>Cerca il tuo prossimo volo</h1>
      </header>

      <nav className="app-nav">
        <button onClick={() => fetchQuery("/aeroporti")}>Voli Fuori Italia</button>
        <button onClick={() => fetchQuery("/vol.sopra.med")}>Voli in Italia</button>
        <button onClick={() => fetchQuery("/serv.api")}>Tutti Voli</button>
      </nav>
          

<main className="app-main">
        {error && <p className="error-message">Errore: {error}</p>}
        {risultato && (
          <div className="result-container">
            <h2>Risultato:</h2>
            <ul>
              {risultato.map(([id, compagnia, prezzo], index) => (
                <li key={index}>
                  <strong>ID:</strong> {id} | <strong>Compagnia:</strong> {compagnia} | <strong>Prezzo:</strong> {prezzo}€
                </li>
              ))}
            </ul>
          </div>
        )}
      </main>
    </div>
  );
};
export default App;