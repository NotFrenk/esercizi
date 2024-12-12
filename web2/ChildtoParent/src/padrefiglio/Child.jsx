import React from "react";

function Child({onMessage}) {
   const sendMessagetoParent = () => {
      //invia il messaggio al parent tramite la funzione onMessage
      onMessage('Ciao dal componente Child!')
   };

   return (
      <div>
         <button onClick={sendMessagetoParent}>Invia messaggio al Parent</button>
      </div>
   );
};

export default Child