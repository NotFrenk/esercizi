
// array dinamici ... 
let numeri = [];

numeri.push("1");
numeri.push(2);
numeri.push(3);
numeri.push("ciao");
// empty
numeri[10] = 20;

let numeri2 = new Array();

if(numeri[0] == 1){ // == ===
    console.log("entra");
    
}

let x = true;
let y = 1;

if(x == y){
    console.log("entra");
}

// && di corto circuito
// || !

if(x == y || x < 10){

}

if(x == y & x < 10){
    
}

let b = 10;

// let m = b++;
console.log("testdiprova");

console.log((b++)+""+(b==11));  // 11 no
//11
console.log("testdiprova2");
console.log(b+=1); // 12 si