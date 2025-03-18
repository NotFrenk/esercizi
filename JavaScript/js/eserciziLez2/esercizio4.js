
let anni = "50";

document.getElementById("testo").innerHTML = anni + typeof(anni);

// funzione globale ... funzione di js ... nel core
document.getElementById("testo1").innerHTML = typeof(anni) == "number";

// isNaN ...
// NaN costante : Not a Number
console.log("ciao" * 10); // NaN ... 
document.getElementById("testo2").innerHTML = isNaN(anni);  // true se non è un numero

// cast ... parseInt() parseFloat()
parseInt(anni); // number 50

let giorni = 'Lunedi, Martedi, Mercoledi, Giovedi, Venerdi, Sabato, Domenica';

giorni = giorni.replaceAll(',' , '\n');

console.log(giorni);
