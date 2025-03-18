
function inParametri(num){
   return num>=1 && num<=7;
}

function settimana(num){
   if (inParametri(num)){
      const giorniSettimana = ["Lunedì", "Martedì", "Mercoledì", 
            "Giovedì", "Venerdì", "Sabato", "Domenica"
         ];
         return `Il giorno corrispondente è : ${giorniSettimana[num -1]}`;
   }
   else {
      return "Peccato, non posso indovinare il giorno."
   }

}




// Test delle funzioni
console.log(settimana(3));  // Output: Il giorno corrispondente è: Mercoledì
console.log(settimana(7));  // Output: Il giorno corrispondente è: Domenica
console.log(settimana(10)); // Output: Peccato, non posso indovinare il giorno.
console.log(settimana(0));  // Output: Peccato, non posso indovinare il giorno.
