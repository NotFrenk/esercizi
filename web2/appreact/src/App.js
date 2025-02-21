import logo from './logo.svg';
import './App.css';
import Esempio1 from './examples/Esempio1';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Esempio1>
          
        </Esempio1>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
