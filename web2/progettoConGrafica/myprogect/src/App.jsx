const App = () => {
  const [risultato, setRisultato] = useState(null);
  const [error, setError] = useState(null);
  const [query, setQuery] = useState(""); // Stato per la query personalizzata

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

  const sendCustomQuery = () => {
      fetch(`http://localhost:5001/personalizzata`, {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({ query: query }),
      })
          .then(response => {
              if (!response.ok) {
                  throw new Error(`Errore nella richiesta: ${response.statusText}`);
              }
              return response.json();
          })
          .then(data => {
              setRisultato(data.Risultato);
              setError(null);
          })
          .catch(err => {
              setError(err.message);
              setRisultato(null);
          });
  };

  return (
      <div style={{ padding: "20px" }}>
          <h1>Gestione Query</h1>
          <div>
              <button onClick={() => fetchQuery('/aeroporti')}>Visualizza Aeroporti</button>
              <button onClick={() => fetchQuery('/vol.sopra.med')}>Voli Sopra la Media</button>
              <button onClick={() => fetchQuery('/serv.api')}>Città Servite da Apitalia</button>
          </div>
          <div style={{ marginTop: "20px" }}>
              <h2>Query Personalizzata</h2>
              <input
                  type="text"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Scrivi una query SQL"
                  style={{ width: "300px", marginRight: "10px" }}
              />
              <button onClick={sendCustomQuery}>Esegui Query</button>
          </div>
          <div style={{ marginTop: "20px" }}>
              {error && <p style={{ color: "red" }}>Errore: {error}</p>}
              {risultato && (
                  <div>
                      <h2>Risultato:</h2>
                      <ul>
                          {risultato.map((item, index) => (
                              <li key={index}>{JSON.stringify(item)}</li>
                          ))}
                      </ul>
                  </div>
              )}
          </div>
      </div>
  );
};
