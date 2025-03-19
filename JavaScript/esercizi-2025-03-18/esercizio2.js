
let job = (data) =>{
   return new Promise ( (res, reg) =>{
      if (isNaN(data)){
            reg("ERRORE");
      }
      else if (data % 2 != 0){
         setTimeout(() => {
            res("numero disparo")
         }, 1000);
      }
      else{
         setTimeout(() =>{
            res("numero paro");
         }, 2000);
      }
   });
};

job(1)
.then((x) =>{
   console.log(x);
})
.catch((e) => {
   console.log(e);
})