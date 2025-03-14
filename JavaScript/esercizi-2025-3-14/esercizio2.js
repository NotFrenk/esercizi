let annoCorrente = new Date().getFullYear();
let annoNascita = 2004;

let Anni = annoCorrente - annoNascita;
let per100 = 100 - Anni;


let calcolaAnni = () =>{
   console.log(annoCorrente, Anni, per100)
   document.getElementById("testo1").innerText = `Ho ${Anni} anni.`;
   document.getElementById("testo2").innerText = `Mi mancano ${per100} anni per arrivare a 100.`;
}