test1(); // test1
//test2(); // undefined ...
test3(); // ERRORE 
// funzioni

// fase 1 ... hoisting
function test1() {
    console.log("test1");
}

// test1 funzione (oggetto eseguibile) ... test1 è una variabile
console.log(test1); 
test1();

var test2 = function () {
    console.log("test2");
}

test2();

// FASE 2 ... hoisting ... ES6 ... arrow function ... come callback ... funzioni chiamate automaticamente
let test3 = function () {
    console.log("test3");
}

let test4 = () => {
    console.log("test4");
}

test3();


const test5 = {
    nome : 'Alice',
    saluta : function(){
        console.log("ciao");
    }
}

test5.saluta();

let nuovi = numeri.map( (el) => {
    return el+1;
})

// REGOLE ARROW FUNCTION : 80%
// 1 - SE il parametro è 1 solo le parentesi tonte sono opzionali
// 2 - SE l'istruzione è 1 sola.... le graffe non sono obbligatorie ed il return è implicito

let nuovi2 = numeri.map( el => el+1 )