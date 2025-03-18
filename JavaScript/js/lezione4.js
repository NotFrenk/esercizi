// while    :   a priori NON so quante volte ciclo

// for      :   a priori SO esattamente quante ciclare

let i = 1

while (i <= 10) { 
    console.log(i);
    i++;
}


let numeri = [3,6,9];

// 5 modi for

for(let x = 0 ; x <= 10 ; x++){ // 99% array (100%)
    console.log(x);
}

// ES6 for in ... for of : 
for(let z in numeri){
    console.log(numeri[z]);
}

for(let z of numeri){
    console.log(z);
}

// JS ... Array() ... metodo dell'oggetto Array map() forEach()
let variabile1 = numeri.forEach( (el) => { // NON TORNA NULLA
    console.log(el);
    return el+1;
} );

let variabile2 = numeri.map( (el) => { // TORNA UN NUOVO ARRAY
    console.log(el);
    return el+2;
} );

console.log("valore variabile1 " + variabile1); // undefined
console.log("valore variabile2 " + variabile2); // 5 8 11
