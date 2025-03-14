function calcolaTempo () {
   let secondi  = parseInt(document.getElementById("inputSecondi").value);

   if (isNaN(secondi) || secondi < 0) {
      document.getElementById("risultato").innerText = "Inserisci un numero valido!";
      return;
}

let ore = Math.floor(secondi / 3600);
let minuti = Math.floor((secondi%3600)/60);
let sec = secondi % 60;

document.getElementById("risultato").innerText = `${ore} ore, ${minuti} minuti, ${sec} secondi.`;
}