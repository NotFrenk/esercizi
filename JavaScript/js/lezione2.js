//console.log(x); // undefined
console.log(z);


// FASE 1 - 1994
// HOISTING :   sposta le funzioni in alto alla riga 1
//              sposta le dichiarazioni di variabili in alto
//var x = 10;

//var x = 20;
z = 30;

// FASE 2 - 2009
let y = 10;
//let y = 20;


// javascript : SOLO OGGETTI ... gestiti come primitivi 
let x = 10; // number
let nome = 'Mario' + 'Rossi';
let esito = true;

// FASE 2 - 2009 template string
let cognome = `Il mio compagno ${nome} è di milano`;

let numero1 = "10";
let numero2 = "1";
// cerco di risolverla in modo naturale ... cerca di risolverla forzatamente ... NaN
console.log(numero1 + numero2); // 1020
console.log(numero1 - numero2); // 200
