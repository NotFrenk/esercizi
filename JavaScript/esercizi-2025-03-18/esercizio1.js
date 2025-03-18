let job = () =>{


   return new Promise((resolve,reject) => {
      setTimeout(()=> {
         resolve("hello world");
      }, 2000 );

   });

};

job().then((result)=>{
   console.log(result);
}).catch ((error) => {
   console.error(error);
});