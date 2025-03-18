console.log("codice 1");

// Promise() : oggetto javascript ... creato per gestire le chiamate asincrone
// Promise COSTRUTTORE (metodo particolare) ... input una funzione callback
// il costruttore prende come parametro una funzione che a sua volta prende come parametro 2 funzioni
// funzione OK
// funzione KO

// CODICE PRODUTTORE
let x = new Promise( (resolve,reject) => {

    console.log("codice 2");
    // connetto al db .... recupero gli utenti ... ci sono ?
    let esito = true;
    if(esito){
        setTimeout( () => { // delega 
            console.log("codice 3");
            resolve("tutto ok"); // sinonimo return
        } , 1000);
        
    }else{
        reject("errore nella chiamata"); // sinonimo return
    }
});

console.log("codice 4");

// CODICE CONSUMATORE : stampa a video (document.write)
x.then( (dati) => { // consumata SOLO quando è terminata
    console.log("codice 5");
    console.log(dati); // tutto ok
    
} ).catch( (err) => {
    console.log(err); // errore nella chiamata
    
});

console.log("codice 6");

// 1 2 4 6 3 5 