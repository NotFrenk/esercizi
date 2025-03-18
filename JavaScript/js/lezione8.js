
// Procedura ... 

let a = () => {
    console.log("sono A login");
}

let b = () => { // js
    console.log("sono B"); // js
    setTimeout( () => { 
        console.log("carico gli utenti");
     } , 0 ); // browser delega
}

let c = () => {
    console.log("sono C calcolo il codice fiscale");
}

let d = () => {
    console.log("sono D calcolo la busta paga");
}

let calcolo = () => {
    a(); // login
    b(); // carico gli utenti
    c(); // calcolo il codice fiscale
    d();
}

calcolo();

// js furbo ... usa FUNZIONI non sono le sue (browser) ... (Node.js)
// delega l'ambiente ... 
// setTimeout() fetch()