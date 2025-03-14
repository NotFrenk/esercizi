let x = 10;

let y = x;

let z = "Mario";

let mostraTipo = () =>{
   document.getElementById("testo1").innerText = x + typeof(x);
   document.getElementById("testo2").innerText = y + typeof(y);
   document.getElementById("testo3").innerText = z + typeof(z);
}