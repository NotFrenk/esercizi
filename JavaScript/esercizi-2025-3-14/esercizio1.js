let num1 = 5;
let num2 = 20;
let num3 = 30;
let num4 = 40;
let num5 = 15;

let somma = num1+ num2 + num3 + num4 + num5;
let media = somma/5;

let calcolanum =()=>{
   console.log(somma,media)
   document.getElementById("somma").innerText=`Somma = ${somma}`;
   document.getElementById("media").innerText=`Media = ${media}`;
}