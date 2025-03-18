function sonoIdentici(a,b){
   return a===b ;
}

// Test della funzione
console.log(sonoIdentici(5, 5));      // true
console.log(sonoIdentici(5, "5"));    // false
console.log(sonoIdentici("ciao", "ciao")); // true
console.log(sonoIdentici(true, 1));   // false
console.log(sonoIdentici(null, undefined)); // false